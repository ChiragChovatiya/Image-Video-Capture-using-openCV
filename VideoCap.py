import cv2

vid = cv2.VideoCapture(0)

# We need to check if camera
# is opened previously or not
if (vid.isOpened() == False):
	print("Error reading video file")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('VideoS.avi',
						cv2.VideoWriter_fourcc(*'MJPG'),
						10, size)
	
while(True):
	ret, frame = vid.read()

	if ret == True:

		result.write(frame)

		# Display the frame
		# saved in the file
		cv2.imshow('Frame', frame)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	else:
		break

vid.release()
result.release()
	
cv2.destroyAllWindows()

print("The video was successfully saved")
