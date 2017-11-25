# PV248 Python, Group 2
# Part 7 - Basic linear algebra with NumPy
# Branislav Smik
# 16.10.2017
#
#
# numpy.hsplit(array, [2])

import re # regular expressions
import sqlite3
import json
import sys
import numpy

FILE1 = 'matrix1.txt'
FILE2 = 'matrix2.txt'

def main():
    #PART1
    data = numpy.loadtxt(FILE1)
    print(data)

    determinant = numpy.linalg.det(data)
    print("determinant = {}".format(determinant))

    inverse = numpy.linalg.inv(data)
    print("inverse: \n{}".format(inverse))

    #----------------------------------------
    #PART2
    data2 = numpy.loadtxt(FILE2)
    print("matrix2: \n{}".format(data2))

    coeff = numpy.hsplit(data2, [len(data2[0])-1]) #resp. dim-1

    solved = numpy.linalg.solve(coeff[0], coeff[1])
    print("Solved matrix2: \n{}".format(solved))


if __name__ == "__main__":
    main()