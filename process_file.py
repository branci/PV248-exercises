# PV248 Python, Skupina 2
# Part1 - Text & Regular expressions
# Branislav Smik

from collections import Counter
import re
import os
import sys

# os.path.join(sys.path[0], 'some file.txt') ... path to the current folder

FILENAME = 'scorelib.txt'
FILEPATH = os.path.join(sys.path[0], FILENAME)

def parseFile(filePath):
    file = open(filePath, mode='r', encoding='utf8')
    authorsCounter = Counter()
    cMinorKeyCount = 0

    for line in file:
        splitLine = line.split(':')

        if(splitLine[0] == 'Composer'):
            authorsCounter[splitLine[1].strip()] += 1

        key = re.findall(r"c min", line, re.IGNORECASE)
        if(key):
            cMinorKeyCount += 1

    print("Number of pieces for each composer:")
    for key, value in authorsCounter.items():
        print("Name: {}, Pieces: {}".format(key, value))
    print("Number of pieces in C minor key: {}".format(cMinorKeyCount))


def main():
    parseFile(FILEPATH)

if __name__ == "__main__":
    main()
