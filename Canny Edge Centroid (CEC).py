import numpy as np
import cv2
import timeit
import time
import math

    


font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

dgppx = 0.09375 #for 56 degrees setting



'''init
         [a] mm
        o - -
         \   | [b] mm
     leg1 \  |
           O x
          /  |
    leg2 /   | [c] mm
        /    |
       o- - -x
        [d] mm
''' 

a = 40
b = 25
c = 75
d = 73
focallength = 10.5 #mm
def CalculateSetup(a,b,c,d):
    leg1 = math.sqrt(a**2+b**2)
    leg2 = math.sqrt(c**2+d**2)
    leg_ad = math.sqrt((d-a)**2 + (b+c)**2)

    
    return [leg1,leg2, leg_ad]

realHeight = float(CalculateSetup(a,b,c,d)[2])

print(CalculateSetup(a,b,c,d))
while(True):

    start = time.time()
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ret, mask = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
    mask = cv2.GaussianBlur(mask,(9,9),0)
    mask = cv2.Canny(mask, 100, 200)
    
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    coordlist = []
    for c in cnts:
        M = cv2.moments(c)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            
            if len(coordlist) < 3:
                coordlist.append((cX,cY))
        except ZeroDivisionError:
            pass
    try: 
        dot1= coordlist[0]
        dot2 = coordlist[1]
        dot3 = coordlist[2]
    except IndexError:
        pass


    
    for i in coordlist:
        cv2.putText(mask,str(coordlist.index(i)+1),i, font, 2,(255,255,255),2,cv2.LINE_AA)


    '''
    REKENGEDEELTE
         40mm
        o - -
         \   | 25mm
          \  |
           O x
          /  |
         /   | 75mm
        /    |
       o- - -x
         73mm
    ''' 

    try:
        yout = ((focallength*realHeight*height)/((math.sqrt(abs(dot3[0]-dot1[0])**2)+(dot3[1]-dot1[1])**2))*1.476)
        xout = dot2[0]
        #print(yout)
        #print(xout)
    except NameError or TypeError or ZeroDivisionError as e:
        #print(e)
        pass

    cv2.imshow('detected circles',mask)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    print(-1/float(start-time.time())) #Om tijd te meten
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
