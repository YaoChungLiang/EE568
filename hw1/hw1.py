import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2
def p2():
    # a
    img=cv2.imread('./1_4.bmp')
    cv2.imshow("Lady M",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # b
    print(img.dtype) # uint8 : unsigned int 8
    
    #b
    img = np.asarray(img, dtype=float)
    print(img.dtype) # float64
    cv2.imshow("Lady M",img)  
    # mostly white, 0 = black, 1 = white and any other value out of range clipped
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def p3():
    # a
    img = cv2.imread('./1_3.tif')
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #p2()
    p3()
