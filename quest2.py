# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:44:47 2018

@author: shorav
"""

import cv2

import numpy as np

a=cv2.imread("02.png")

b= cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

_,c= cv2.threshold(b,200,255,cv2.THRESH_BINARY)

contor = cv2.findContours(c.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print contor
cv2.imshow("Image",c)
cv2.waitKey(0)
cv2.destroyAllWindows()