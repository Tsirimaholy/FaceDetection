import cv2
from random import randrange

# load some pre-trained data on face frontal from opencv (haaar cascade algorithm)
# and use them to detect faces
trained_face_data = cv2.CascadeClassifier('./train_data/haarcascade_frontalface_default.xml')

# choose image to detect faces in
img = cv2.imread('./test.jpg')

# convert to grayscale to determine the face coordinate easily
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces coordinates
# Detected objects are returned as a list of rectangles
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# surround the faces with rectangles using all coordinates
for (x, y, w, h) in face_coordinates:
	cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 3)


# display the image on a window
cv2.imshow('python image detection', img)

# prevent the window from automatically close
cv2.waitKey()

# save the image with all face surrounded by rectangles
# cv2.imwrite('image.jpeg', img)
print("code completed")