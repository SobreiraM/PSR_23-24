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
