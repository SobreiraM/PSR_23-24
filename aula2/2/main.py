#!/usr/bin/env python3
# --------------------------------------------------

from my_functions import isPerfect

maximum_number = 500  # maximum number to test.

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()