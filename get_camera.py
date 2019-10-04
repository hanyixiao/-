#codeing by Hanyixiao
#SDU 
import cv2
import time
import numpy
cap = cv2.VideoCapture(10)
frameIndex=0;
time_last=0;
while 1:
    ret, frame = cap.read()
    #frame = cv2.imread("output/frame-{}.png".format(frameIndex))
    cv2.imshow("cap", frame)
    frameIndex +=1
    print("[HanInfo:]FPS",1/(time.time()-time_last))
    time_last=time.time();
   # time.sleep(1)
    print(frameIndex)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
