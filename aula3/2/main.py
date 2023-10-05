#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
from math import sqrt
import colorama 
from colorama import Fore, Back, Style

def addComplex(x, y):
    sum = (x[0]+y[0],x[1]+y[1])
    return sum

def multiplyComplex(x, y):
    mul = (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    return mul

def printComplex(x):
    print(str(x[0]) + " + " + str(x[1]) + "i")

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()