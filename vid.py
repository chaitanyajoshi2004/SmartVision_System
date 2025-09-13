
import numpy as np
import cv2

capture=cv2.VideoCapture("github video.mp4")

if (capture.isOpened()==False):
            print("error opening vedio")

def make_1080p():
        capture.set(3,1920)
        capture.set(4,1080)

def make_720p():
        capture.set(3,1280)
        capture.set(4,720)


def make_480p():
        capture.set(3,640)
        capture.set(4,480)
def c_r(w,h):
    capture.set(3,w)
    capture.set(4,h)
make_1080p()

while (capture.isOpened()):
            ret,frame=capture.read()
            if ret==True:
                cv2.imshow("frame",frame)
                if cv2.waitKey(25) & 0xFF==ord('q'):
                    break
            else:
                    break
capture.release()
cv2.destroyAllWindows()
