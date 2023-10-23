#!/usr/bin/env python
import cv2

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    while True:

        _, image = capture.read()  # get an image from the camera

        # add code to show acquired image
        
        cv2.imshow(window_name, image)
        if cv2.waitKey(25) == ord(' '):
            break
        # add code to wait for a key press

    capture.release()
    cv2.destroyAllWindows()
    
    

if __name__ == '__main__':
    main()