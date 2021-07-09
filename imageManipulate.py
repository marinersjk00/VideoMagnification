# Creator: Jordan Kuschner
# Created on: July 8, 2021
import cv2
import numpy as np


# loading the original image
original = cv2.imread('Mike_Trout.jpeg')  # reading the image file
cv2.imshow('original image', original)
cv2.waitKey(0) # press any key to close

print(original.shape)  # prints dimensions of original image (height, width, RGB channels)

# resizing the image
r = 9000 / original.shape[0]
dim = (int(original.shape[1] * r), 9000)

# creating new image with altered dimensions
resizedImage = cv2.resize(original, dim, interpolation=cv2.INTER_AREA)  #performing actual resizing
cv2.imshow('resized image', resizedImage)  # displaying resized image
cv2.waitKey(0)

# rotating an image
(h, w) = original.shape[:2]
center = (w / 2, h / 2)  # point of rotation
degreeRotate = 180.0

matrix = cv2.getRotationMatrix2D(center, degreeRotate, 1.0)  # setting up rotation
rotatedImage = cv2.warpAffine(original, matrix, (w, h))  # performing actual rotation
cv2.imshow('rotated image', rotatedImage)
cv2.waitKey(0)

# cropping an image
croppedImage = original[100:200, 200:400]
cv2.imshow('cropped image', croppedImage)
cv2.waitKey(0)

# saving image to disk
  #  cv2.imwrite('filename.jpg', imageVar)



