import cv2 as cv 
import mediapipe as mp 
import numpy as np 
import cv2 as cv 

class handTrack:
	def __init__(self, number):
		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(static_image_mode = False, max_num_hands = number, min_detection_confidence = 0.90)
		self.mpDraw = mp.solutions.drawing_utils
		self.board = np.ones(shape = (480, 640, 3), dtype = "uint8") * 0

	def capture(self, camID):
		cap = cv.VideoCapture(camID)
		while (1):
			_, self.frame = cap.read()
			self.frame = cv.flip(self.frame, flipCode = 1)
			imgRGB = cv.cvtColor(src = self.frame, code = cv.COLOR_BGR2RGB)
			results = self.hands.process(imgRGB)
			if (results.multi_hand_landmarks != None):
				for handsLandMarks in results.multi_hand_landmarks:
					for i, lm in enumerate(handsLandMarks.landmark):
						h, w, c = imgRGB.shape
						self.cx, self.cy = int(lm.x * w), int(lm.y * h)
						if (i == 8):
							self.drawBoard()
							print (i, self.cx, self.cy)
				#self.mpDraw.draw_landmarks(self.frame, results.multi_hand_landmarks[0], self.mpHands.HAND_CONNECTIONS)
			cv.imshow("Sketch", self.board)
			#cv.imshow("droid", self.frame)
			key = cv.waitKey(1)
			if (key == 13):#the if condition for detecting the cporrect key
				break
			if (key == 8):
				self.board = np.ones(shape = (480, 640, 3), dtype = "uint8") * 0

		cap.release()

	def drawBoard(self):
		cv.circle(self.board, center = (self.cx, self.cy), radius = 5, color = (0, 255, 0), thickness = -1)
		#cv.line(self.board, pt1 = (self.cx, self.cy), pt2 = (self.cx + 1, self.cy + 1), color = (255, 0, 0), thickness = 10)



obj = handTrack(1)
obj.capture(0)

