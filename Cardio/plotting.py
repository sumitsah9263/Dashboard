import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import os
import json
from datetime import date

def plott(folderpath, time_axis_ecg, normalised_valueInt, time_axis_pcg, normalised):
    from pylab import rcParams
    rcParams['figure.figsize'] = 20, 10

    fig, (ax1, ax2) = plt.subplots(2, 1)

    plt.setp(ax1.spines.values(), linewidth=5)
    plt.setp(ax2.spines.values(), linewidth=5)

    ax1.set_xticks(np.arange(0, 20, 0.4))

    ax1.tick_params(labelsize=18)
    ax2.tick_params(labelsize=18)

    ax1.plot(time_axis_ecg, normalised_valueInt)
    ax1.set_ylabel("ECG", fontsize=18)

    ax2.plot(time_axis_pcg, normalised)
    ax2.set_xlabel("Time (in secs.)", fontsize=18)
    ax2.set_ylabel("PCG", fontsize=18)

    plt.subplots_adjust(hspace=.0)

    name = "result.png"
    newpath = os.path.join(folderpath, name)

    plt.savefig(newpath, bbox_inches='tight', format='png', pad_inches=0.2, orientation='landscape')


def plotting(folderpath, time_axis_ecg, normalised_valueInt, normalised, r_peaks_time, r_peaks, p_time, p_values, t_time, t_values, t_end_time, t_end_values, t_start_time, t_start_values, Q_time, Q_values, S_time, S_values, show_r, show_p, show_q, show_t, show_s, time_axis_pcg, envelope_filtered, peak_time_s1, peak_s1, peak_time_s2, peak_s2, s1_width_time, s2_width_time):
    # To increase the size of the figure plot
    from pylab import rcParams
    rcParams['figure.figsize'] = 20, 10

    fig, (ax1, ax2) = plt.subplots(2, 1)

    plt.setp(ax1.spines.values(), linewidth=5)
    plt.setp(ax2.spines.values(), linewidth=5)

    ax1.set_xticks(np.arange(0, 20, 0.4))
    ax1.tick_params(labelsize=18)
    ax2.tick_params(labelsize=18)
    # Turn on the minor ticks on
    ax1.minorticks_on()

    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.grid(which='major', linestyle='-', linewidth='0.5', color=(1, 0, 0))
    ax1.grid(which='minor', linestyle='-', linewidth='0.4', color=(1, 0.7, 0.7))

    #plt.setp(ax1.get_xticklabels(), visible=True)
    # Plotting the Data
    ax1.plot(time_axis_ecg, normalised_valueInt)

    # Plotting R-Peaks
    if show_r:
        ax1.plot(r_peaks_time, normalised_valueInt[r_peaks], '.', label='R')
    else:
        print('R-Peaks Not Detected (Improper Signal)')

    # Plotting P-Peaks
    if show_p:
        ax1.plot(p_time, normalised_valueInt[p_values], "x", label='P')
    else:
        print('P-Peaks Not Detected (Improper Signal)')

    # Plotting T-Peaks
    if show_t:
        ax1.plot(t_time, normalised_valueInt[t_values], "o", label='T')
    else:
        print('T-Peaks Not Detected (Improper Signal)')

    '''#Plotting T-End Points
    plt.plot(t_end_time, normalised_valueInt[t_end_values], "*",label='T-End')

    #Plotting T-Start Points
    plt.plot(t_start_time, normalised_valueInt[t_start_values], "D",label='T-Start')'''

    # Plotting Q-Peaks
    if show_q:
        ax1.plot(Q_time, normalised_valueInt[Q_values], "+", label='Q')
    else:
        print('Q-Peaks Not Detected (Improper Signal)')

    # Plotting S-Peaks
    if show_s:
        ax1.plot(S_time, normalised_valueInt[S_values], "^", label='S')
    else:
        print('S-Peaks Not Detected (Improper Signal)')

    ax1.legend(loc="upper left")
    ax1.set_ylabel("ECG", fontsize=18)

    ax2.plot(time_axis_pcg, normalised)

    #ax2.plot(peak_time_s1, envelope_filtered[peak_s1], 'r.', label='S1')
    #ax2.plot(peak_time_s2, envelope_filtered[peak_s2], '*', label='S2')

    plt.vlines(s1_width_time, -0.003, 0.003, linestyles="dashed", colors="g")
    plt.vlines(s2_width_time, -0.0015, 0.0015, linestyles="dotted", colors="r")

    ax2.set_xlabel("Time (in secs.)", fontsize=18)
    ax2.set_ylabel("PCG", fontsize=18)
    plt.subplots_adjust(hspace=.0)

    name = "result.png"
    newpath = os.path.join(folderpath, name)
    plt.savefig(newpath, bbox_inches = 'tight', format = 'png', pad_inches = 0.2, orientation = 'landscape')

    plott(folderpath, time_axis_ecg, normalised_valueInt, time_axis_pcg, normalised)
