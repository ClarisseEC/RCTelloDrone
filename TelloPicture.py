import time
import cv2
from djitellopy import Tello

tello_obj = Tello()
tello_obj.connect()
tello_obj.streamon()

tello_video = cv2.VideoCapture('udp://@0.0.0.0:11111')

scale = 3
while True:
    ret, frame = tello_video.read()
    if ret:
        height, width, layers = frame.shape
        new_h = int(height / scale)
        new_w = int(width / scale)
        resize = cv2.resize(frame, (new_w, new_h))
        cv2.imshow('Tello', resize)

        # Take picture when "m" is pressed
        if cv2.waitKey(1) & 0xFF == ord('m'):
            # Get current timestamp
            current_time = time.strftime('%Y%m%d-%H%M%S')
            # Save image with timestamp as filename
            filename = f'tello-{current_time}.jpg'
            cv2.imwrite(filename, resize)
            print(f'Saved image: {filename}')

    # End program when "/" is pressed
    if cv2.waitKey(1) & 0xFF == ord('/'):
        break

tello_obj.streamoff()
tello_video.release()
cv2.destroyAllWindows()
