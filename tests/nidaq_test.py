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

from src.Controller.ni_daq import NIDAQ, PXI6733
import pytest
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy import signal
import math


# @pytest.mark.run_this

@pytest.fixture
def get_daq() -> NIDAQ:
    return NIDAQ()


@pytest.fixture
def get_pxi6733() -> PXI6733:
    return PXI6733()


def test_nidaq(capsys):
    daq = NIDAQ()
    dev_list = daq.get_connected_devices()
    for d in dev_list:
        with capsys.disabled():
            print(d)


def test_pxi6733_connection():
    daq = PXI6733()
    assert daq.is_connected

def test_pxi6733_connection2(get_pxi6733):
    assert get_pxi6733.is_connected
@pytest.mark.run_this
def test_pxi6733_ctrout():
    daq = PXI6733()
    clk_task = daq.setup_clock('ctr0', 1000)
    print('clktask: ', clk_task)
    time.sleep(0.1)
    daq.run(clk_task)
    daq.wait_to_finish(clk_task)
    daq.stop(clk_task)

@pytest.mark.run_this
def test_pxi6733_ctrout(get_pxi6733):
    daq = get_pxi6733
    clk_task = daq.setup_clock('ctr0', 1000)
    print('clktask: ', clk_task)
    time.sleep(0.1)
    daq.run(clk_task)
    daq.wait_to_finish(clk_task)
    daq.stop(clk_task)

@pytest.mark.parametrize("ext_clock", [True, False])
def test_pxi6733_ctr_read(capsys, get_pxi6733,ext_clock):
    daq = get_pxi6733
    ctr_task = daq.setup_counter('ctr0', 50, use_external_clock=ext_clock)
    samp_rate = daq.tasklist[ctr_task]['sample_rate']
    time.sleep(0.1)
    daq.run(ctr_task)
    time.sleep(0.1)
    data, nums = daq.read(ctr_task)
    daq.stop(ctr_task)
    avg_counts_per_bin = np.diff(data).mean()
    # daq.wait_to_finish(ctr_task)


    with capsys.disabled():
        print('ctrtask: ', ctr_task)
        print(data)
        print('the sampling rate was {}'.format(samp_rate))
        print("The avg counts per bin was {}".format(avg_counts_per_bin))
        print("The counting rate is {} cts/sec".format(avg_counts_per_bin * samp_rate))

@pytest.mark.parametrize("ext_clock", [True, False])
def test_pxi6733_ao_ctr_read(capsys, get_pxi6733,ext_clock):
    daq = get_pxi6733
    ctr_task = daq.setup_counter('ctr0', 50, use_external_clock=ext_clock)

    samp_rate = 20000.0

    period = 1e-3
    t_end = period

    num_samples = math.ceil(t_end * samp_rate / 2.) * 2  # for AO, it appears only even sample numbers allowed
    t_array = np.linspace(0, t_end, num_samples)
    waveform = np.sin(2 * np.pi * t_array / period)
    waveform2 = signal.sawtooth(2 * np.pi * t_array / period, 0.5) + 1

    ao_task = daq.setup_AO(["ao0"],waveform2,clk_source=ctr_task)
    samp_rate = daq.tasklist[ctr_task]['sample_rate']
    time.sleep(0.1)
    daq.run(ao_task)
    daq.run(ctr_task)
    time.sleep(0.1)
    data, nums = daq.read(ctr_task)
    daq.stop(ao_task)
    daq.stop(ctr_task)
    avg_counts_per_bin = np.diff(data).mean()
    # daq.wait_to_finish(ctr_task)


    with capsys.disabled():
        print('ctrtask: ', ctr_task)
        print(data)
        print('the sampling rate was {}'.format(samp_rate))
        print("The avg counts per bin was {}".format(avg_counts_per_bin))
        print("The counting rate is {} cts/sec".format(avg_counts_per_bin * samp_rate))