import numpy as np
import cv2
import timeit
import time
import imutils
import re

cap = cv2.VideoCapture(0)

while(True):

    now = time.time()
    start = timeit.timeit()
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray,55,255,cv2.THRESH_BINARY)

    contours= cv2.Canny(mask,100,200)

    print(now - time.time())
    






    
    cv2.imshow('frame',contours)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
