#!/usr/bin/env python3
# --------------------------------------------------

import argparse
from my_functions import isPerfect

maximum_number = 500  # maximum number to test.

def main():
    #Process command line arguments
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-mn','--maximum_number',type=int, help='max_number.')
    parser.add_argument ('-n', '--name', type=str, help='A name to print.')

    args = vars(parser.parse_args())
    print(args)

    print() #completar ex 3

    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()