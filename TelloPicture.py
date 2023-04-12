#
# --- (c) 02/2020 f41ardu
#
# Tello cam using opencv proof of concept
# https://tellopilots.com/threads/taking-pictures-with-tello-drone-using-python-3.4964/
#
#

# import opencv 4.2.0
from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()
tello.streamon()

telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")

# wait for frame
ret = False
# scale down
scale = 3

while (True):
    # Capture frame-by-framestreamon
    ret, frame = telloVideo.read()
    if (ret):
        # Our operations on the frame come here
        height, width, layers = frame.shape
        new_h = int(height / scale)
        new_w = int(width / scale)
        resize = cv2.resize(frame, (new_w, new_h))  # <- resize for improved performance
        # Display the resulting frame
        cv2.imshow('Tello', resize)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        cv2.imwrite("C:\Users\danny\OneDrive\Desktop\python stuff\pythonProject\StoredPics'\'test.jpg", resize)  # writes image test.bmp to disk
        print("Take Picture")

    if cv2.waitKey(1) & 0xFF == ord('/'):
        break

# When everything done, release the capture
telloVideo.release()
cv2.destroyAllWindows()
