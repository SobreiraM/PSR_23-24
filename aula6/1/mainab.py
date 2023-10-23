import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    
    #a)
    h, w, c = image.shape
    x = w//2
    y = h//2
    image_dot = cv2.circle(image, (x,y), 5, (0,0,255),-1)

    #b)
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50,100)
    fontscale = 3
    color = (0,0,255)
    thickness = 2
    image_dot = cv2.putText(image_dot, 'PSR', org, font,  
                   fontscale, color, thickness, cv2.LINE_AA)
    

    cv2.imshow('window', image_dot)
    cv2.waitKey(0)
    cv2.destroyWindow('window')


if __name__ == '__main__':
    main()