import numpy as np
import cv2

def Get_Limits(color):
    
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerlimit = hsvC[0][0][0] - 10,170,20
    upperlimit = hsvC[0][0][0] + 10,255,255

    lowerlimit = np.array(lowerlimit, dtype = np.uint8)
    upperlimit = np.array(upperlimit, dtype = np.uint8)

    return lowerlimit, upperlimit