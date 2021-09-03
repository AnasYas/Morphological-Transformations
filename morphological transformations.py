import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('balls.jpg',0)
_,mask=cv2.threshold(img,220,225,cv2.THRESH_BINARY_INV)
kernal=np.zeros((2,2),np.uint8)
dilation=cv2.dilate(mask,kernal,iterations=1)
erosion=cv2.erode(mask,kernal,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal,iterations=1)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal,iterations=1)
cv2.imshow('gray img',img)
cv2.imshow('mask',mask)
cv2.imshow('after dilation',dilation)
cv2.imshow('after erosion',erosion)
cv2.imshow('after opening',opening)
cv2.imshow('after closing',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
