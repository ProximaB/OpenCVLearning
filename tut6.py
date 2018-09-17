import cv2
import numpy as np

img = cv2.imread('book.jpg') #above 160 white, under black

retval, threshold = cv2.threshold(img, 130 , 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 130 , 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
retval2, otsu = cv2.threshold(grayscaled, 100 , 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('optional', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold ofter grayscaled', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWinows() 