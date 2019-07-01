import cv2

video_capture = cv2.VideoCapture(0)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = video_capture.read()

cv2.imwrite('testing.png', video_capture.read()[1])

# Close device
video_capture.release()

