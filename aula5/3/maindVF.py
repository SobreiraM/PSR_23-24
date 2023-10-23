import cv2
import argparse
import numpy
from functools import partial
import json
import pprint



def onTrackbar(min_B, max_B, min_G, max_G, min_R, max_R, image_hsv):

    min_B = cv2.getTrackbarPos('min B/H', 'window - Ex3a')
    max_B = cv2.getTrackbarPos('max B/H', 'window - Ex3a')
    min_G = cv2.getTrackbarPos('min G/S', 'window - Ex3a')
    max_G = cv2.getTrackbarPos('max G/S', 'window - Ex3a')
    min_R = cv2.getTrackbarPos('min R/V', 'window - Ex3a')
    max_R = cv2.getTrackbarPos('max R/V', 'window - Ex3a')

    print(str(min_B), end=' ')
    print(str(max_B), end=' ')
    print(str(min_G), end=' ')
    print(str(max_G), end=' ')
    print(str(min_R), end=' ')
    print(str(max_R))

    mask = cv2.inRange(image_hsv, (min_B,min_G,min_R), (max_B,max_G,max_R))
    cv2.imshow('window - Ex3a', mask)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('-u_HSV', '--use_HSV', help='Formato de imagem.', action='store_true')
    args = vars(parser.parse_args())
    cv2.namedWindow('window - Ex3a')


    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    if args['use_HSV']:
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        new_image = image_hsv
        print("HSV format")
    else:
        new_image = image
        print("RGB format")


    cv2.imshow('Original', image)

    cv2.createTrackbar('min B/H', 'window - Ex3a', 0, 255, 
                       lambda x : onTrackbar(x,0,0,0,0,0,new_image))

    cv2.createTrackbar('max B/H', 'window - Ex3a', 0, 255,
                       lambda x : onTrackbar(0,x,0,0,0,0,new_image))
    
    cv2.createTrackbar('min G/S', 'window - Ex3a', 0, 255, 
                       lambda x : onTrackbar(0,0,x,0,0,0,new_image))
    
    cv2.createTrackbar('max G/S', 'window - Ex3a', 0, 255,  
                       lambda x : onTrackbar(0,0,0,x,0,0,new_image))
    
    cv2.createTrackbar('min R/V', 'window - Ex3a', 0, 255, 
                       lambda x : onTrackbar(0,0,0,0,x,0,new_image))
    
    cv2.createTrackbar('max R/V', 'window - Ex3a', 0, 255, 
                       lambda x : onTrackbar(0,0,0,0,0,x,new_image))

    onTrackbar(0, 0, 0, 0, 0, 0, new_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()