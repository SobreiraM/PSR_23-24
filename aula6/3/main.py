#!/usr/bin/env python
import cv2
import pathlib
import numpy as np



def main():
    # initial setup
    cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / 'data/haarcascade_frontalface_default.xml'
    print(cascade_path)

    clf = cv2.CascadeClassifier(str(cascade_path))

    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)



    while True:

        _, image = capture.read()  # get an image from the camera
        overlay = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to gray to apply cascadeClassifier and mask


        #---------------------------------- Face identification and surrounding edges ----------------------------------#
        # create face identifying filter
        faces = clf.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(150,150), flags=cv2.CASCADE_SCALE_IMAGE)

        #create rectangle around detected faces and outline edges that are no included in face
        max_area = 0
        max_face = None
        image_new = image

        for (x, y, width, height) in faces: #find the larger area recognised as a face
            if width*height > max_area:
                max_area = width*height
                max_face = (x,y,width,height)

        mask = np.zeros_like(gray) 
        if max_face is not None:
            x,y,width,height = max_face
            cv2.rectangle(overlay, (x,y), (x+width,y+height), (0,200,0), -1)
            mask[y:y+height, x:x+width] = gray[y:y+height, x:x+width]
            image_new = cv2.addWeighted(overlay, 0.5, image, 0.5, 0)
        
        edges = cv2.Canny(gray-mask, 100, 200)

        image_new[np.where(edges > 0)] = [0,0,255]




        #---------------------------------- Speak Detection ----------------------------------#


        #---------------------------------- Images Display ----------------------------------#
        cv2.imshow(window_name, image_new)
        cv2.imshow('mask', mask)
        cv2.imshow('gray', gray)
        if cv2.waitKey(25) == ord(' '):
            break
        

    capture.release()
    cv2.destroyAllWindows()
    
    

if __name__ == '__main__':
    main()