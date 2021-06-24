import cv2

img = cv2.imread('Image.jpg',0)

cv2.imwrite('BWimage.png',img)

cv2.imshow('Image converted into GrayScale',img)

cv2.waitKey(0)

cv2.destroyAllWindows()