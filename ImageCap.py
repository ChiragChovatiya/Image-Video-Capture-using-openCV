import cv2

vid = cv2.VideoCapture(0)
result = True

while(result):
    ret,frame = vid.read()
    cv2.imwrite("Image.jpg",frame)
    result = False
    
vid.release()
cv2.destroyAllWindows()