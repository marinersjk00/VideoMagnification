import cv2
import numpy as np
import glob
from PIL import Image


image_list = []
fileFolder = glob.glob('/Users/jskuschner/PycharmProjects/vidManip/venv/lib/frames/*.jpg')
for file in fileFolder:
   #  print('in the loop')
    image_list.append(cv2.imread(file))

print(image_list)
image1 = image_list[0]
i = 1
for i in range(0, len(image_list)):
    image2 = image_list[i]
    diff = cv2.subtract(image1, image2)  # if they are the same, diff will be all 0
    cv2.imshow('comparing...', diff)
    cv2.waitKey(1)
    image1 = image2
    i = i + 1


