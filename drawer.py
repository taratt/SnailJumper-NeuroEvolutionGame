import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
def plot_stats():
    lines = []
    num_lines = []
    with open('generations.txt') as f:
        for line in f:
            lines.append(line.split())

        for line in lines:
            num_line = []
            for i in line:
                num_line.append(float(i))
            num_lines.append(num_line)

    maxs = np.array([x[0] for x in num_lines])
    avgs = np.array([x[1] for x in num_lines])
    mins = np.array([x[2] for x in num_lines])
    generations = np.arange(len(num_lines))

    fig, ax = plt.subplots(1, 3)
    ax[0].plot(generations, maxs, 'tab:orange')
    ax[0].set_title("Maximum fitness")
    ax[0].set(xlabel ="generation" , ylabel= "maxs")

    ax[1].plot(generations, avgs, 'tab:green')
    ax[1].set_title("average of fitnesses")
    ax[1].set(xlabel="generation", ylabel="avgs")

    ax[2].plot(generations, mins,'tab:red')
    ax[2].set_title("Minimum fitness")
    ax[2].set(xlabel ="generation" , ylabel= "mins")

    # ax.xaxis.set_major_locator(MultipleLocator(2))
    # ax.yaxis.set_major_locator(MultipleLocator(20))
    # ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    # ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    # ax[0,0].grid(which='minor', color='#CCCCCC', linestyle='--')


    plt.show()



