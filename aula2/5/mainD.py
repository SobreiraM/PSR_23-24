#!/usr/bin/env python3
# --------------------------------------------------

import readchar

def countNumbersUpTo(stop_char):
    numbers = []
    
    print('Start typing! If you press "X" the program will end')
    while True:
        key = readchar.readkey()
        if key.isnumeric():
            numbers.append(key)
        
        print('you typed '+key)

        if key==stop_char:
            break
    
    print('List of the numeric values inserted')
    print(numbers)

    print('List of the numeric values inserted after sorting')
    numbers.sort()
    print(numbers)





def main():

    countNumbersUpTo('X')

if __name__ == '__main__':
    main()