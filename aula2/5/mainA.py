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
    

    total_numbers = 0
    total_others = 0
    for key in keys:
        if key.isnumeric():
            total_numbers += 1
        else:
            total_others += 1

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')




def main():

    countNumbersUpTo('X')

if __name__ == '__main__':
    main()