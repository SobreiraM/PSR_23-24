#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
import colorama 
from colorama import Fore, Back, Style

#initialize colorama
colorama.init(autoreset=True)


maximum_number = 10
def isPrime(value):
    for i in range(2,value):
        if value%i==0:
            return False
        
    return True


def main():

    print("Starting to compute prime numbers up to " + str(maximum_number))
    

    for i in range(0, maximum_number):
        if isPrime(i):
            print('Number ' + Fore.GREEN + str(i) + Style.RESET_ALL +  ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')
            print('Dividers (rest = 0):'),
            for k in range(1,i+1):
                if i%k==0:
                    print(str(k), end=" ")
            print("")

if __name__ == "__main__":
    main()