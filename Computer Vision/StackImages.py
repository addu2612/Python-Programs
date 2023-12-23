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

img = cv.imread("Photos/Lenna.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imgStack = stackImages(0.5, [[img, img_gray, img], [img, img, img_gray]])

cv.imshow("Stack", imgStack)
cv.waitKey(0)
