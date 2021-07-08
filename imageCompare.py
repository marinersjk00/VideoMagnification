# Creator: Jordan Kuschner
# Created on: July 8, 2021
import cv2
import numpy as np

image1 = cv2.imread('/Users/jskuschner/PycharmProjects/pythonProject1/venv/lib/frames/DonAndDan1282.jpg')  # first image to be compared
image2 = cv2.imread('/Users/jskuschner/PycharmProjects/pythonProject1/venv/lib/frames/DonAndDan1269.jpg')  # second image to be compared

diff = cv2.subtract(image1, image2)  # if they are the same, diff will be all 0

result = not np.any(diff)

if result is True:
    print("The images are the same")
else:
    print("The images are different")
    cv2.imwrite('different.jpg', diff)
