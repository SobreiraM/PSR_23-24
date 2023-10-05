#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style

Complex = namedtuple("Complex", ['real','imag'])

def addComplex(x, y):
    sum = Complex(x.real + y.real ,x.imag + y.imag)
    return sum

def multiplyComplex(x, y):
    mul = Complex(x.real * y.real - x.imag * y.imag, x.real * y.imag + x.imag * y.real)
    return mul

def printComplex(x):
    print(str(x))

def main():


    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)
    c2 = Complex(-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()