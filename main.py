import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()
fps = cvzone.FPS()

listImg = os.listdir("images")
imgList = []

for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    imgBg = cv2.resize(img, (640,480))
    imgList.append(imgBg )

imgIndex = 0
while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[imgIndex], threshold = 0.5)

    imgStacked = cvzone.stackImages([img,imgOut],2,1)
    fps.update(imgStacked)
    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if imgIndex > 0:
            imgIndex -= 1
    elif key == ord('d'):
        if imgImdex < len(imgList)-1:
            imgIndex += 1
    elif key == ord('q'):
        break