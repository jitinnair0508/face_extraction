import cv2
import os
import natsort


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(r'C:\Users\Dell\Desktop\Haar Face Extraction\1_1_01_1.avi')
t=0
while True:
    
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_color = img[y+2:y+h-2, x+2:x+w-2]

    cv2.imwrite("C:/Users/Dell/Desktop/folder4/{}.png".format(t), roi_color)
    t=t+1



filelist=os.listdir('C:/Users/Dell/Desktop/folder4')
for fichier in filelist[:]: 
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
print(natsort.natsorted(filelist,reverse=False))