#!/usr/bin/env python3
# --------------------------------------------------

maximum_number = 500  # maximum number to test.


def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    dividers = []

    for i in range(1,value):
        if value%i == 0:
            dividers.append(i)
        
    return dividers


def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
    # <Add stuff here>
    dividers = getDividers(value)

    return value == sum(dividers)


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()