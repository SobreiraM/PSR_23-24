#!/usr/bin/env python3
# --------------------------------------------------

import readchar

def countNumbersUpTo(stop_char):
    ordem = 1
    dicio = {}

    print('Start typing! If you press "X" the program will end')
    while True:
        key = readchar.readkey()
        if not(key.isnumeric()):
            dicio[ordem] = {key}
        
        print('you typed '+key)
        ordem += 1
        if key==stop_char:
            break
    
    print('The dictionary created with non-numeric inputs is the following:')
    print(dicio)




def main():

    countNumbersUpTo('X')

if __name__ == '__main__':
    main()