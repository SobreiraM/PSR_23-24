#!/usr/bin/env python3
# --------------------------------------------------

import readchar

def countNumbersUpTo(stop_char):
    keys = []
    
    print('Start typing! If you press "X" the program will end')
    while True:
        key = readchar.readkey()
        keys.append(key)


        
        print('you typed '+key)

        if key==stop_char:
            break
    
    print('List of the inputs inserted')
    print(keys)

    numbers = [item for item in keys if item.isnumeric()]
    print('List of numeric inputs inserted')
    print(numbers)




def main():

    countNumbersUpTo('X')

if __name__ == '__main__':
    main()