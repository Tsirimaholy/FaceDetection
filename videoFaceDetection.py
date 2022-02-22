import cv2
from random import randrange

# load some pre-trained data on face frontal from opencv (haaar cascade algorithm)
# and use them to detect faces
trained_face_data = cv2.CascadeClassifier('./TrainData/haarcascade_frontalface_default.xml')

# instead of img wwe open each frame
# webcam = cv2.VideoCapture('video.mp4')

webcam = cv2.VideoCapture(0)

# iterate forrever over frame
while True:
	# Read current frame
	(succesful_frame_read, frame) = webcam.read()
	# convert to grayscale
	grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# determine the face coordinate
	face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

	for (x, y, w, h) in face_coordinates:
    	#  draw rectangle on the current rgb frame
		cv2.rectangle(frame, (x, y), (x + w, y + h), (128, 56, 25), 3)

	# display the video on a window
	cv2.imshow('python image detection', frame)
	# while loop will continue automaticaly every 1 milliseconde
	key = cv2.waitKey(1)
	# wait that user press the key "q or Q" to close the window
	if key == 81 | key == 113:
		break

# release the video capture effect
webcam.release()
print('code completed')