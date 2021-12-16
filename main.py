import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

while True:
    success, ing = cap.read()
    img = detector.findHands(img)
    inlist,_= detector.findPosition(img)
    cv2.inshow("image", ing)
    cv2.waitkey(1)

