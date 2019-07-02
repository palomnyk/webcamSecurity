import cv2
import datetime

datetime.datetime.now()

video_capture = cv2.VideoCapture(0)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = video_capture.read()

cv2.imwrite(f'securityPic{datetime.datetime.now()}.png', video_capture.read()[1])

# Close device
video_capture.release()

