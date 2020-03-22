import numpy as np
import cv2
import matplotlib.pyplot as plt

image_path = 'C:/Users/raych/Computer Vision/OpenCV/Images/fgbg.jpg'

image = cv2.imread(image_path, -1)
print(image.shape[:2])

mask = np.zeros(image.shape[:2], np.uint8)

# Usually of shape (1, 65) and of type float64
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Must include the foreground object
rect = (820, 230, 200, 500)

# This will modify the mask image and label pixels with 4 flags denoting background or foreground as such
# cv.GC_BGD - an obvious background pixel   - 0
# cv.GC_FGD - an obvious foreground pixel   - 1
# cv.PR_BGD - a possible background pixel   - 2
# cv.PR_FGD - a possible foreground pixel   - 3
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 15, cv2.GC_INIT_WITH_RECT)

# Here, we take the sure and possible background pixels and set to 0, otherwise 1
mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
image = image * mask2[:, :, np.newaxis]

plt.subplot(121), plt.imshow(image)
plt.title('Grabcut'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread(image_path, -1), cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.show()
