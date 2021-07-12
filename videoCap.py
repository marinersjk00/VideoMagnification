# Creator: Jordan Kuschner
# Created on: July 8, 2021
import cv2

cap = cv2.VideoCapture('/Users/jskuschner/Desktop/plants.mov')  # 0 for webcam, or for existing video file replace 0 with 'absolute_file_path'
i = 0
while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('Community', frame)
    path = '/Users/jskuschner/PycharmProjects/vidManip/venv/lib/frames/plant' + str(i) + '.jpg'  # images will be saved into frames folder as .jpg files
    cv2.imwrite(path, frame)  # saves current frame to specified path above
    i += 1  # increments index to differentiate between frames quickly
cap.release()
cv2.destroyAllWindows()