import cv2
import numpy as np

#video=cv2.VideoCapture("Ultraedge1.mp4")
video=cv2.VideoCapture("ultraEdge.mp4")


while True :
    ret,frame=video.read()
    frame=cv2.resize(frame,(690,590))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edeges=cv2.Canny(gray,18,180)

    cv2.imshow("canny",edeges)
    #cv2.imshow("original",frame)
    cv2.imshow("lines",frame) 

    k=cv2.waitKey(25)
    if k == ord("c") :
        break



video.release()    
cv2.destroyAllWindows()

