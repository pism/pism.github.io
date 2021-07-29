#!/usr/bin/env python3
#
# (C) 2014--2020 Andy Aschwanden, Ed Bueler, Constantine Khrulev
#
# XKCD-style plot of pism publications per year.

from pybtex.database import parse_file, BibliographyData
import numpy as np
import matplotlib.pylab as plt
import sys

def get_year(bib_data, year):
    D = {}
    for k, v in bib_data.entries.items():
        if int(v.fields["year"]) == year:
            D[k] = v
    return BibliographyData(D)

def years(bib_data):
    result = []
    for _, v in bib_data.entries.items():
        result.append(int(v.fields["year"]))
    return set(result)

def plot(year, no_of_pubs, output_file):
    bar_width = 0.5
    offset = bar_width
    ymax = no_of_pubs.max() + 1

    plt.xkcd(scale=1, length=100, randomness=1)
    fig, ax = plt.subplots()

    ax.bar(year + offset, no_of_pubs,
           bar_width, color="#C6DBEF", edgecolor="#3182BD", linewidth=2.5)

    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    ax.set_ylim([0, ymax])
    ax.set_xlim([np.min(year), np.max(year) + 1.0])

    ax.set_xlabel("year", fontsize=16)
    ax.xaxis.set_ticks(year + offset)
    ax.xaxis.set_ticklabels([str(y) for y in year])
    ax.yaxis.set_ticks(np.arange(0, ymax + 1, 3))

    fig.tight_layout()

    ax.set_title(f"Number of PISM publications ({sum(no_of_pubs)} so far)")

    ticklabels = ax.get_xticklabels()
    for tick in ticklabels:
        tick.set_rotation(90)

    fig.savefig(output_file, bbox_inches="tight")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = parse_file(input_file)

    Y = years(data)

    N = max(Y) - min(Y) + 1
    year = np.linspace(min(Y), max(Y), N, dtype=int)
    no_of_pubs = np.zeros_like(year)

    for k in range(N):
        year_data = get_year(data, year[k])
        no_of_pubs[k] = len(year_data.entries)

    plot(year, no_of_pubs, output_file)
