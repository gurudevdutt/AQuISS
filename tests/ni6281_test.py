# Created by Gurudev Dutt <gdutt@pitt.edu> on 2023-08-03
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from src.Controller.ni_daq import NIDAQ, PXI6733,NI6281
import pytest
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy import signal
import math




@pytest.fixture
def get_nidaq() -> NIDAQ:
    # create a fixture for the NIDAQ
    return NIDAQ()


@pytest.fixture
def get_pxi6733() -> PXI6733:
    # create a fixture for the PXI6733
    return PXI6733()

@pytest.fixture
def get_ni6281() -> NI6281:
    # create a fixture for the PXI6733
    return NI6281()

def test_ni6281_connection(get_ni6281):
    """This test checks if ni6281 is connected
    Passed successfully
    - GD 10/05/2023
    """
    assert get_ni6281.is_connected

@pytest.mark.parametrize("channel",["ao0","ao1"])
def test_ni6281_analog_out(get_ni6281,channel):
    """This test has passed successfully for both AO0 and Ao1. it outputs AO voltages on a single channel
    - GD 10/05/2023"""
    daq = get_ni6281
    samp_rate = 20000.0

    period = 1e-3
    t_end = period

    num_samples = math.ceil(t_end * samp_rate / 2.) * 2  # for AO, it appears only even sample numbers allowed
    t_array = np.linspace(0, t_end, num_samples)
    waveform = np.sin(2 * np.pi * t_array / period)
    waveform2 = signal.sawtooth(2 * np.pi * t_array / period, 0.5) + 1
    ao_task = daq.setup_AO([channel],waveform2)
    daq.run(ao_task)
    daq.wait_to_finish(ao_task)
    daq.stop(ao_task)

@pytest.mark.parametrize("channel",["ao0","ao1"])
@pytest.mark.parametrize("voltage",[-1.0,0.0,1.0,0.0])
def test_ni6281_analog_dcvoltage(capsys,get_ni6281,channel,voltage):
    """This test has passed successfully for both AO0 and Ao1. it outputs a single DC voltage on a single channel
        - GD 10/05/2023"""
    daq = get_ni6281
    with capsys.disabled():
        print("NI6281 AOchannel  = {0} , voltage = {1} ".format(channel,voltage))
        time.sleep(1.0)
    daq.set_analog_voltages({channel:voltage})

def test_ni6281_ctrout(get_ni6281):
    """This test has passed successfully. It outputs a waveform on the ctr0 output
    - GD 10/05/2023"""
    daq = get_ni6281
    clk_task = daq.setup_clock('ctr1', 100)
    print('clktask: ', clk_task)
    time.sleep(0.1)
    daq.run(clk_task)
    daq.wait_to_finish(clk_task)
    daq.stop(clk_task)
def test_ni6281_ctr_read(capsys, get_ni6281):
    """This test reads finite samples from ctr0 using internal hardware timed clock
    Test has passed successfully !
    - GD 10/06/2023"""
    daq = get_ni6281
    ctr_task = daq.setup_counter('ctr0', 50)
    samp_rate = daq.tasklist[ctr_task]['sample_rate']
    time.sleep(0.1)
    daq.run(ctr_task)
    time.sleep(0.1)
    data, nums = daq.read(ctr_task)
    #daq.wait_to_finish(ctr_task)
    avg_counts_per_bin = np.diff(data).mean()
    daq.stop(ctr_task)
    with capsys.disabled():
        print('ctrtask: ', ctr_task)
        print(data)
        print('the sampling rate was {}'.format(samp_rate))
        print("The avg counts per bin was {}".format(avg_counts_per_bin))
        print("The counting rate is {} cts/sec".format(avg_counts_per_bin * samp_rate))


def test_ni6281_ai_read(capsys, get_ni6281):
    """This test reads finite samples from AI0, using a hardware
    timed clock from ctr0
    Test has passed successfully !
    - GD 10/06/2023"""
    daq = get_ni6281
    clk_task = daq.setup_clock('ctr1', 1000)
    ai_task = daq.setup_AI('ai0', clk_source=clk_task, num_samples_to_acquire=50)
    samp_rate = daq.tasklist[clk_task]['sample_rate']
    time.sleep(0.1)
    t1 = time.perf_counter()
    daq.run([ai_task, clk_task])
    daq.wait_to_finish(clk_task)
    data, num_samples = daq.read(ai_task)

    X = np.arange(0, num_samples)
    avg_volts_per_bin = np.mean(data)

    with capsys.disabled():
        print('AItask: ', ai_task)
        print(num_samples)
        print(data)
        print("The avg volts read was {}".format(avg_volts_per_bin))
        plt.plot(X, data[0], color='r', label='AI0')
        # plt.plot(X, data[1, :], color='g', label='AI1')
        plt.show()
