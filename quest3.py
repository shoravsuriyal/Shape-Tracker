import numpy as np
import cv2
import os

total_features=0

lis= os.listdir("c:\Users\shorav\Desktop\images")

def analyze_frame():

    counter=0
    rflag=1
    tflag=1
    sflag=1
    cflag=1s

    for im in lis:

        counter+=1
        img = cv2.imread(im)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur= cv2.medianBlur(gray,5)
        cimg = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)

        gray = np.float32(gray)

        corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 5)
        corners = np.int0(corners)
        print "frame number : "+str(counter)
        print "Number of corners detected: "+str(len(corners))
        circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=50,minRadius=0,maxRadius=0)
        if len(corners)==4 and flag is not None:

            print 'The unique figure is RECTANGLE'
            flag=None

        elif len(corners)==7 and tflag is not None:

            print 'The unique figure detected is Triangle'
            tflag=None

        elif len(corners)==
            
        print circles
        print 'circle detected'
        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(img,(x,y),3,255,-1)
        

        print '-----------------'

        if circles is not None:

            
            for i in circles[0,:]:
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        else:
            pass

if __name__=='__main__':

    analyze_frame()
    cv2.imshow('Corner',img)
    cv2.imshow('Circle',blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


