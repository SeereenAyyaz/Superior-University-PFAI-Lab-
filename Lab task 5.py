# Author: Seereen
# Description: Demonstration of major OpenCV functions
# using the image of Ma Dong Seok
# --------------------------------------------

import cv2
import numpy as np

# Path to your image
img_path = "C:\\Users\\T L S\\Downloads\\Ma Dong Seok.jpeg"

# Read the image
image = cv2.imread(img_path)

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# -------------------- 1. Display Original Image --------------------
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# -------------------- 2. Resize and Crop --------------------
resized_img = cv2.resize(image, (300, 200))
cropped_img = image[50:200, 100:300]

cv2.imshow("Resized Image", resized_img)
cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)

# -------------------- 3. Color Space Conversion --------------------
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Gray Scale", gray_img)
cv2.imshow("HSV Color Space", hsv_img)
cv2.waitKey(0)

# -------------------- 4. Drawing Shapes and Text --------------------
draw_img = image.copy()
cv2.line(draw_img, (50, 50), (250, 50), (0, 255, 0), 3)
cv2.rectangle(draw_img, (60, 100), (200, 200), (255, 0, 0), 2)
cv2.circle(draw_img, (150, 150), 40, (0, 0, 255), -1)
cv2.putText(draw_img, "Ma Dong Seok", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow("Drawing Shapes & Text", draw_img)
cv2.waitKey(0)

# -------------------- 5. Image Thresholding --------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Simple Thresholding", thresh1)
cv2.imshow("Adaptive Thresholding", thresh2)
cv2.waitKey(0)

# -------------------- 6. Edge Detection --------------------
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Edge Detection using Canny", edges)
cv2.waitKey(0)

# -------------------- 7. Contours & Shape Detection --------------------
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_img = image.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

cv2.imshow("Contours & Shape Detection", contour_img)
cv2.waitKey(0)

# -------------------- 8. Face Detection --------------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray_face = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_face, scaleFactor=1.1, minNeighbors=5)

face_detect = image.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(face_detect, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Face Detection", face_detect)
cv2.waitKey(0)

# -------------------- 9. Write (Save) Images --------------------
cv2.imwrite("C:\\Users\\T L S\\Downloads\\Saved_Ma_Dong_Seok.jpeg", image)
print("Processed image saved successfully in Downloads.")
cv2.destroyAllWindows()
