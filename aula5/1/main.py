#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
from time import time, sleep
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style
import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='OpenCV testing...')

    parser.add_argument('-img1', type=str, help='Submit path to png file', required = True)
    parser.add_argument('-img2', type=str, help='Submit path to png file', required = True) 
    
    args = vars(parser.parse_args())

    switch_f = 0
    image_filename1 = args['img1']
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image

    image_filename2 = args['img2']
    image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR) # Load an image

    while 1:
        if switch_f == 0:
            cv2.imshow('window1', image1)  # Display the image
            switch_f = 1
            cv2.waitKey(3000)
        else:
            cv2.imshow('window1', image2)  # Display the image
            switch_f = 0
            cv2.waitKey(3000)              # wait for a key press before proceeding


if __name__ == '__main__':
    main()