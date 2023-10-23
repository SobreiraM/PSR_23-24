import argparse
import cv2
import numpy as np
from functools import partial
import colorama 
from colorama import Fore, Back, Style


def mouseCallback(event, x, y, flags, *userdata, image, drawing_data):
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_data['pencil_down'] = True
        print('pencil_down set to True')
    elif event == cv2.EVENT_LBUTTONUP:
        drawing_data['pencil_down'] = False
        print('pencil_down set to False')

    # Place to code the drawing part
    if drawing_data['pencil_down'] == True:
        cv2.line(image,(drawing_data['previous_x'],drawing_data['previous_y']), (x,y),
                 drawing_data['color'], 1)
        
    drawing_data['previous_x'] = x
    drawing_data['previous_y'] = y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    drawing_data = {'pencil_down': False, 'previous_x': 0, 'precious_y': 0, 'color': (255,255,255)}

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', partial(mouseCallback, image=image, drawing_data=drawing_data))
    
 
    while True:

        cv2.imshow('image', image)
        key = cv2.waitKey(25)
        
        if key == 32:
            break
        if key == ord('r'):
            print(Fore.RED + 'Changing pencil to red color' + Style.RESET_ALL)
            drawing_data['color'] = (0,0,255)
        if key == ord('b'):
            print(Fore.BLUE + 'Changing pencil to blue color' + Style.RESET_ALL)
            drawing_data['color'] = (255,0,0)
        if key == ord('g'):
            print(Fore.GREEN + 'Changing pencil to green color' + Style.RESET_ALL)
            drawing_data['color'] = (0,255,0)



    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()