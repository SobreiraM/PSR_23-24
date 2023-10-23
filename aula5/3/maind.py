import argparse
import cv2
from functools import partial


def onTrackbar(image_hsv, window_name, data):
    # Add code here t image_gray and show image in window
    pass
    



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window'
    Bmax = Bmin = Gmax = Gmin = Rmax = Rmin = 120
    data = {'minBlue': Bmin, 'minGreen': Gmin, 'minRed': Rmin, 'maxBlue': Bmax, 'maxGreen': Gmax, 'maxRed': Rmax}

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    onTrackbar(image_hsv,window_name,data)

    # add code to create the trackbar ...
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Bmax', window_name, 0, 255,    
                partial(onTrackbar,image_hsv=image_hsv, window_name=window_name, data=data))
    
    cv2.createTrackbar('Bmin', window_name, 0, 255,    
                partial(onTrackbar,image_hsv=image_hsv, window_name=window_name, data=data))
    
    cv2.createTrackbar('Gmax', window_name, 0,255,    
                partial(onTrackbar,image_hsv=image_hsv, window_name=window_name, data=data))
    
    cv2.createTrackbar('Gmin', window_name, 0, 255,    
                partial(onTrackbar,image_hsv=image_hsv, window_name=window_name, data=data))
    
    cv2.createTrackbar('Rmax', window_name, 0, 255,    
                partial(onTrackbar,image_hsv=image_hsv, window_name=window_name, data=data))
    
    cv2.createTrackbar('Rmin', window_name, 0, 255,    
                partial(onTrackbar,image_hsv=image_hsv, window_name=window_name, data=data))
    
    while(1):
        mask = cv2.inRange(image_hsv, (data['minBlue'],data['minGreen'],data['minRed']),
                        (data['maxBlue'],data['maxGreen'],data['maxRed']))
        cv2.imshow(window_name, mask)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 32:
            break

        Bmax = cv2.getTrackbarPos('Bmax', window_name)
        Bmin = cv2.getTrackbarPos('Bmin', window_name)
        Gmax = cv2.getTrackbarPos('Gmax', window_name)
        Gmin = cv2.getTrackbarPos('Gmin', window_name)
        Rmax = cv2.getTrackbarPos('Rmax', window_name)
        Rmin = cv2.getTrackbarPos('Rmin', window_name)
    
    cv2.destroyAllWindows()
    

    

if __name__ == '__main__':
    main()