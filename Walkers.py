import cv2


# Create our body classifier
face_cascade = cv2.CascadeClassifier('C:/Python310/Lib/site-packages/opencv-4.x/data/haarcascades/haarcascade_fullbody_alt.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    body = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in faces:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
