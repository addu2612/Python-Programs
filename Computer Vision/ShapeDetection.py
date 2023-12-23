import cv2 as cv
import numpy as np

def stackImages(scale, imgArray, labels=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                imgArray[x][y] = cv.resize(imgArray[x][y], (width, height), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        hor = [np.hstack(imgArray[x]) for x in range(rows)]
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            imgArray[x] = cv.resize(imgArray[x], (width, height), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
 
    if len(labels) != 0:
        eachImgWidth = int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)

        for d in range(rows):
            for c in range(cols):
                cv.rectangle(ver, (c * eachImgWidth, eachImgHeight * d),
                             (c * eachImgWidth + len(labels[d][c]) * 13 + 27, 30 + eachImgHeight * d),
                             (255, 255, 255), cv.FILLED)
                cv.putText(ver, labels[d][c], (eachImgWidth * c + 10, eachImgHeight * d + 20),
                           cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 255), 2)

    return ver

def getContours(img):
    contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv.contourArea(cnt)
        print(area)
        if area>500:
            cv.drawContours(img_contour,cnt,-1,(0 ,0,255),3)
            peri=cv.arcLength(cnt,True)
            approx=cv.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv.boundingRect(approx)

            if objCor==3: objectType="Triangle"
            elif objCor==4: 
                AspRat=w/float(h)
                if AspRat>0.95 and AspRat<1.05:
                    objectType="Square"
                else:
                    objectType="Rectangle"    
            elif objCor>4:
                objectType="Circle"        
            else: objectType="None"
             

            cv.rectangle(img_contour,(x,y),((x+w),(y+h)),(255,153,255),5)
            cv.putText(img_contour,objectType,(x+(w//2)-10,y+(h//2)-10),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)



img=cv.imread("Photos/Screenshot 2023-12-23 at 5.55.03 PM.png")
img_contour=img.copy()
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img_blur=cv.GaussianBlur(img_gray,(7,7),1)
img_canny=cv.Canny(img_blur,50,50)
img_blank=np.zeros_like(img)

getContours(img_canny)

img_Stack=stackImages(0.8,([img,img_gray,img_blur],[img_canny,img_contour,img_blank]))
cv.imshow("Stack",img_Stack)
cv.waitKey(0)