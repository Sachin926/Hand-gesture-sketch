import cv2 as cv
import mediapipe as mp
import time
import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode = False,
 	max_num_hands = 1, min_detection_confidence = 0.5)	#This class uses only RGB image code i the input imag format
mpDraw = mp.solutions.drawing_utils

while (1):
	_, frame = cap.read()
	imgRGB = cv.cvtColor(src = frame, code = cv.COLOR_BGR2RGB)
	results = hands.process(imgRGB)
	if (results.multi_hand_landmarks != None):
		for handsLandMarks in results.multi_hand_landmarks:
			for i, lm in enumerate(handsLandMarks.landmark):
				h, w, c = imgRGB.shape
				cx, cy = int(lm.x * w), int(lm.y * h)
				print (i, cx, cy)

		mpDraw.draw_landmarks(frame, results.multi_hand_landmarks[0], mpHands.HAND_CONNECTIONS)
	cv.imshow("droidCam", frame)
	key = cv.waitKey(1)
	if (key == 13):
		break
cap.release()