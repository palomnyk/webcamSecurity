import cv2
import datetime
import os

now = datetime.datetime.now()

#windows doesn't permit ":" in the file name
now = str(now).replace(':', '-')

video_capture = cv2.VideoCapture(0)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = video_capture.read()

#for putting code in the same dir as this script
dir_path = os.path.dirname(os.path.realpath(__file__))

pic_path = os.path.join(dir_path, f"securityPic{now}.png")

print(pic_path)

cv2.imwrite(pic_path, video_capture.read()[1])

# Close device
video_capture.release()
