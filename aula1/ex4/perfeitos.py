#!/usr/bin/env python3
#shebang line

a maria inês é muito linda
maximum_number = 100

def isPerfect(value):
    sum = 0

    for i in range(1,value):
        if value%i==0:
            sum += i   #somar numeros cuja divisão por value tenha resto 0
            
        if sum==value:
            return True
        
    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
