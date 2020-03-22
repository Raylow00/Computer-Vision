import numpy as np
import cv2
import matplotlib.pyplot as plt

image_path = 'C:/Users/raych/Computer Vision/OpenCV/Images/drone.jpg'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# run a threshold on the image to divide into blacks and whites
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# remove noise from image by applying morphologyEx transformation
# Opening - another name for erosion then dilation - useful in removing noises
# Closing - dilation then erosion - useful in closing small holes
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# now we dilate the result to find the sure backgrounds
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# obtain sure foregrounds by applying distanceTransform and then threshold
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.1*dist_transform.max(), 255, 0)
# this is the threshold value to compare against, those greater will be turned into 255, else 0
print(0.7*dist_transform.max())

# we have sure fg and sure bg
# we find the unknown areas by subtracting sure fg from sure bg
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# create a marker (an array of the same size as the image) and label the regions inside it
ret, markers = cv2.connectedComponents(sure_fg)

markers = markers + 1
markers[unknown==255] = 0

# apply watershed, boundary pixels will be marked with label -1
markers = cv2.watershed(image, markers)
image[markers == -1] = [255, 0, 0]

cv2.imshow("Sure bg", sure_bg)
cv2.imshow("Sure fg", sure_fg)
cv2.imshow("Distance transform", dist_transform)
cv2.imshow("Unknown", unknown)

plt.imshow(image)
plt.show()