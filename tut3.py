import numpy as np
import cv2

img = cv2.imread('merida.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (60, 0, 60), 10)
cv2.rectangle(img, (15,25), (200,150), (), 5)
cv2.circle(img, (100,63), 55, (0,0,255), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 2.5, (100,0,0), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(10*1000)
cv2.destroyAllWindows()