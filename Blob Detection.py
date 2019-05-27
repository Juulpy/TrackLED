import numpy as np
import cv2
import timeit
import time
import imutils
import re
import math
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

while(True):
    start = time.time()
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ret, mask = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
    mask = cv2.GaussianBlur(mask,(9,9),0)
    
    # Orb magic (blob detection)
    orb = cv2.ORB_create()    

    kp1, des1 = orb.detectAndCompute(mask, None)

    mask = cv2.drawKeypoints(mask,kp1,mask,color=(255,255,0), flags=0) #markeer de kp's

    #pts is een numpy-array van alle points, ook de points die we niet nodig hebben
    pts = (np.asarray([[p.pt[0], p.pt[1]] for p in kp1])).tolist()
    print('-------------------')
    if len(pts) is not 0:

        def dot(nr):
            try:
                return int(pts[nr+1][0]),int(pts[nr+1][1])
            except IndexError:
                return (0,0)
        def distance(): #Calculate distance between dots

            cv2.circle(mask,dot(1), 10, (0,0,255), 1) #Teken een rode cirkel rond het eerste punt

            print(dot(1))
        distance()

        

    '''
    if len(dot1 and dot2 and dot3) > 0: #Om er voor te zorgen dat de waarden niet null zijn (anders crasht ie)
        x1 = dot1[0][0] #Omdat dot1 een embedded list is, moet eerst de eerste (en enige) list gekozen worden met dot1[0] en daarna de value.
        y1 = dot1[0][1]
        
        x2 = dot2[0][0]
        y2 = dot2[0][1]
        
        x3 = dot3[0][0]
        y3 = dot3[0][1]
        
        try:
            y1old #als y1old nog niet bestaat (eerste paar loops), skip deze stap ff 
        except NameError:
            pass
        else:
            if abs(int(y1)-int(y1old)) > 40:
                print('glitchy!')


                        
        text1 = str(str(x1) + "," + str(y1) + '   p1') #de text# variabelen zijn voor de coordinaten en de point index voor de output
        
        text2 = str(str(x2) + "," + str(y2)+ '   p2')

        text3 = str(str(x3) + "," + str(y3)+ '   p3')



        #dingen tekenen
        cv2.circle(mask,(int(x1),int(y1)), 10, (0,0,255), 1) #Teken een rode cirkel rond het eerste punt
        cv2.putText(mask,text1,(int(x1+10),int(y1)), font, 0.5,(255,255,255),2,cv2.LINE_AA) #Teken een cirkel om het tweede punt

        cv2.circle(mask,(int(x2),int(y2)), 10, (0,0,255), 1)
        cv2.putText(mask,text2,(int(x2+10),int(y2)), font, 0.5,(255,255,255),2,cv2.LINE_AA)            

        cv2.circle(mask,(int(x3),int(y3)), 10, (0,0,255), 1)
        cv2.putText(mask,text3,(int(x3+10),int(y3)), font, 0.5,(255,255,255),2,cv2.LINE_AA)

        cv2.line(mask,(int(x1),int(y1)),(int(x2),int(y2)),(255,255,255),5)
        cv2.line(mask,(int(x2),int(y2)),(int(x3),int(y3)),(255,255,255),5)


        y1old = y1
        y2old = y2
        
        y1 = 0
        x1 = 0
        '''
    #time.sleep(0.1)
    # Display the resulting frame
    
    cv2.imshow('frame',mask)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #print(-1/float(start-time.time())) #Om tijd te meten
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
