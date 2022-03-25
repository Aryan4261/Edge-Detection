# edge detection
import cv2

img = cv2.imread("D:\panda.jpg")
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
