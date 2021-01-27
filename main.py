#Image Detection
#import cv2
#from random import randrange

#trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('Resources/yoda.jpg')
#img = cv2.imread('Resources/friends.jpg')
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#face_coorinates = trained_face_data.detectMultiScale(grayscaled_img)

#print(face_coorinates)
#for (x, y, w, h) in face_coorinates:
     #cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128,256), randrange(128, 255), randrange(128, 255)), 2)

#cv2.imshow('output', img)
#cv2.waitKey()

#print("Code Complete")


#Image Detection
import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)
while True:
     successful_frame_read, frame = webcam.read()
     grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     face_coorinates = trained_face_data.detectMultiScale(grayscaled_img)
     for (x, y, w, h) in face_coorinates:
          cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
     cv2.imshow('output', frame)
     key = cv2.waitKey(1)

     if key==81 or key==113:
          break
webcam.release()


