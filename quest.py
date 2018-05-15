

# for finding contour in an image 
'''
import cv2

import numpy as np

a=cv2.imread("02.png")

b= cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

_,c= cv2.threshold(b,200,255,cv2.THRESH_BINARY)

inverted = cv2.bitwise_not(c)

_,contor,_ = cv2.findContours(inverted.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)


cv2.drawContours(a,contor,-1,(0,255,0),6)

cv2.imshow("Image",a)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# the code for the fist method ends here ******************

# code 2
'''
import cv2

import numpy as np

a=cv2.imread("19.png")

b= cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

gray = np.float32(b)
dst = cv2.cornerHarris(gray,5,3,0.04)
    
dst = cv2.dilate(dst,None)

a[dst>0.01*dst.max()]=[0,0,255]
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

res = np.hstack((centroids,corners))
res = np.int0(res)
a[res[:,1],res[:,0]]=[255,0,0]
a[res[:,3],res[:,2]] = [255,0,0]

cv2.imshow("Image",a)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''    
# this code ends here

# Code 3

'''
import cv2

import numpy as np

import os



a=cv2.imread("05.png")

b= cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

_,c= cv2.threshold(b,200,255,cv2.THRESH_BINARY)

inverted = cv2.bitwise_not(c)

_,contor,_ = cv2.findContours(inverted.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

lis=[]
unique=[]


for g in contor:

    area= cv2.contourArea(g)
    if area in lis:

        pass
    else:

        lis.append(area)
    

cv2.imshow("Image",a)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#code 4

import numpy as np
import cv2

import os

lis= os.listdir("c:\Users\shorav\Desktop\images")

f_p = dict( maxCorners = 1,
            qualityLevel = 0.3,
            minDistance = 7,
            useHarrisDetector=True,
            blockSize = 7 )

lk_p = dict( winSize  = (15,15),
             maxLevel = 2,
             criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
o_f= cv2.imread("02.png")
color = np.random.randint(0,255,(100,3))
o_g = cv2.cvtColor(o_f, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(o_g, mask = None, **f_p)

mask = np.zeros_like(o_f)
for img in lis:

    frame = cv2.imread(img)
    f_g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    p1, st, err = cv2.calcOpticalFlowPyrLK(o_g, f_g, p0, None, **lk_p)

    g_n = p1[st==1]
    g_o = p0[st==1]

    for i,(new,old) in enumerate(zip(g_n,g_o)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img2 = cv2.add(frame,mask)
    cv2.imshow('Test',img2)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    o_g = f_g.copy()
    p0 = g_n.reshape(-1,1,2)
cv2.destroyAllWindows()
cap.release()
'''















