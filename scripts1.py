import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(r'C:\Users\Dell\Desktop\Haar Face Extraction\1_1_01_1.avi')
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
t=0
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_color = img[y+3:y+h-3, x+3:x+w-3]
    # Display
    cv2.imwrite("C:/Users/Dell/Desktop/folder3/{}.png".format(t), roi_color)
    t=t+1
    #cv2.imshow('img', img)
    # Stop if escape key is pressed
    #k = cv2.waitKey(30) & 0xff
    #if k==27:
        #break
# Release the VideoCapture object
#cap.release()
        