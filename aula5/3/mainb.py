import argparse
import cv2
from functools import partial

def mouseCallback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x=' + str(x) + 'y=' + str(y))


def onTrackbar(threshold, image_gray, window_name):
    # Add code here to threshold image_gray and show image in window
    retval, image_gray = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_gray)
    



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex3b'
    threshold = 120

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)


    # add code to create the trackbar ...
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Scale', window_name, threshold, 255,    
                partial(onTrackbar,image_gray=image_gray, window_name=window_name))
    
    cv2.setMouseCallback(window_name, mouseCallback)


    cv2.waitKey(0)
    
    cv2.destroyAllWindows
    

    

if __name__ == '__main__':
    main()