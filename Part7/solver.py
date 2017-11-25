# PV248 Python, Group 2
# Part 7 - Basic linear algebra with NumPy
# Branislav Smik
# 25.11.2017
#
#
# Part 3 of the 7th exercise
# NOTE: this is just an MVP, the input must be ordered equations in the correct format
# (one space between each letter/number/sign...)

import numpy

FILE = 'matrix3.txt'

def main():
    #PART3
    file = open(FILE, "r")
    lines = file.readlines()
    print("Equations:")
    for line in lines:
        print(line)

    vars = read_variables(lines[0])
    numbers = []

    #for line in lines:
    #    words = line.split()
    #    line_nums = [int(n) for n in words if  n.isdigit()]
    #    numbers.append(line_nums)

    for line in lines:
        words = line.split()
        last_sign = '+'
        line_nums = []
        for word in words:
            if not word.isalpha() and not word.isdigit():
                last_sign = word
            elif word.isdigit():
                if last_sign == '-':
                    line_nums.append(int(word) * -1)
                else:
                    line_nums.append(int(word))
        numbers.append(line_nums)

    coeff = numpy.hsplit(numpy.array(numbers), [len(numbers[0])-1])

    solved = numpy.linalg.solve(coeff[0], coeff[1])

    for var,res in zip(vars, solved):
        print("{} = {}".format(var, res[0]))

def read_variables(line):
    variables = []

    while True:
        for word in line:
            if word == '=':
                return variables
            if word.isalpha():
                variables.append(word)

if __name__ == "__main__":
    main()