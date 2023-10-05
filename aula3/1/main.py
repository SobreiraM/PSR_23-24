#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
from math import sqrt
import colorama 
from colorama import Fore, Back, Style

from time import time, ctime


#initialize colorama
colorama.init(autoreset=True)


def main():


    print("Starting to compute...")

    t = ctime()
    print(t)
    t_start = time()
    for i in range(0,50000000):
        a = sqrt(i)

    t_end = time()
    print("Finished computing")
    print("The program's duration was: " + Fore.GREEN+(str(t_end-t_start)) + Style.RESET_ALL + " seconds")

if __name__ == "__main__":
    main()