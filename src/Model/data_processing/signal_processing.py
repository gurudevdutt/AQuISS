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

import numpy as np
import matplotlib.pyplot as plt


def power_spectral_density(x, time_step, freq_range = None):
    """
    returns the *single sided* power spectral density of the time trace x which is sampled at intervals time_step
    Args:
        x (array):  timetrace
        time_step (float): sampling interval of x
        freq_range (array or tuple): frequency range in the form [f_min, f_max] to return only the spectrum within this range

    Returns:

    """
    N = len(x)
    P = 2 * np.abs(np.fft.rfft(x))**2 / N * time_step
    F = np.fft.rfftfreq(len(x), time_step)

    if freq_range is not None:
        brange = np.all([F >= freq_range[0], F <= freq_range[1]], axis=0)
        P = P[brange]
        F = F[brange]

    return F, P

if __name__ == '__main__':
    l = 100

    tmax = 10
    t = np.linspace(0, tmax,l)

    dt = tmax / l
    signal = 2.* np.sin(2*np.pi *t) + np.random.randn(l)
    print(signal)

    plt.plot(t,signal)
    plt.show()