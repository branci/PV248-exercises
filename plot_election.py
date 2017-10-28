# PV248 Python, Group 2
# Part 4 - Plotting with bokeh
# Branislav Smik
# 23.10.2017
#
# OUTPUT: Graph representing data from the czech elections

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import json
import sys
import pprint
from numpy import pi, cumsum
import random

FILEPATH = "election.json"

def main():
    with open(FILEPATH) as json_data:
        data = json.load(json_data)

    data = sorted(data, key= lambda x: x['votes'], reverse=True)

    votes = []
    shares = []
    colors = []
    short_names = []

    for strana in data:
        votes.append(strana["votes"])
        shares.append(strana["share"])

        if strana["share"] < 1:
            pass

        if 'color' not in strana:
            colors.append(rand_color())
        else:
            colors.append(strana["color"])

        if 'short' not in strana:
            short_names.append(strana["name"].split(' ', 1)[0])     #get first word of the name
        else:
            short_names.append(strana["short"])

    numbers = range(1, len(data))

    #Part1 bar plot
    '''
    p = figure(x_range=(0, 15), title='Czech Republic election results')
    p.vbar(x=numbers,
           top=votes,
           width=0.4,
           color=colors)
    show(p)
    '''

    #Part3 pie chart
    starts = []
    ends = []

    for i in range(len(shares)):
        if shares[i] == 0.0:
            shares[i] = 0.001

    shares_sum = cumsum(shares)
    print(shares_sum)

    starts = [(p/100) * 2 * pi for p in shares_sum]
    ends.append(starts[-1])
    for start in starts[2:]:
        ends.append(start)

    print(starts)
    print(ends)

    src = ColumnDataSource(data={'start': starts,
                                 'end': ends,
                                 'color': colors,
                                 'label': short_names})
    p = figure(x_range=(-10, 10))
    p.wedge(x=0, y=0, radius=5,
            start_angle='start',
            end_angle='end',
            color='color',
            legend='label',
            source=src)
    show(p)


def rand_color():
    r = lambda: random.randint(0, 255)
    return('#%02X%02X%02X' % (r(), r(), r()))

if __name__ == "__main__":
    main()