import cv2

img = cv2.imread('Image.jpg',0)

matrix = (9,11)

img_blur = cv2.GaussianBlur(img,matrix,0)

cv2.imshow('Blured Image',img_blur)

cv2.waitKey(0)

cv2.destroyAllWindows()