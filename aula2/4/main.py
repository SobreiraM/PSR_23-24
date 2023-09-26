#!/usr/bin/env python3
# --------------------------------------------------

import readchar


def printAllCharsUpTo(stop_char):
    for i in range(32,ord(stop_char)): #ord converts string to number according to ASCII table
        print(chr(i), end =' ')



def readAllUpTo(stop_char):
    if ord(stop_char)!= 88:
        print(stop_char)
    else:
        print('')
        print('"X" input detected')
        print('Exiting...')
        exit(0)


def countNumbersUpTo(stop_char):
    total_numbers = 0
    total_others = 0
    keys = []

    print('Start typing!')

    while True:
        key = readchar.readkey()
        keys.append(key)
        print('You typed '+key)

        if key==stop_char:
            break
    
    print(keys)

    for key in keys:
        if key.isnumeric():
            total_numbers += 1
        else:
            total_others += 1
            
    print('You entered '+ str(total_numbers) + ' numbers')
    print('You entered '+ str(total_others) + ' others')


def main():
    #a)
    #uncomment to use printAllCharsUpTo function
    '''
    print('Press a key to read char:')
    key = readchar.readkey()
    print('User pressed ' + key)
    printAllCharsUpTo(key)
    '''
    #b)
    '''
    print('Press any key you would like to print!')
    print('The "X" input will close the program')
    while 1:
       key = readchar.readkey()
       readAllUpTo(key)
    '''
    #c
    countNumbersUpTo('X')

if __name__ == '__main__':
    main()