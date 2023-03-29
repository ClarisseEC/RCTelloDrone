# --- (c) 02/2020 f41ardu
#
# Tello cam using opencv proof of concept
#

# import opencv 4.2.0
import cv2

# Open the video capture using the 'with' statement
with cv2.VideoCapture("udp://@0.0.0.0:11111") as telloVideo:
    # Check if the video capture is open
    if not telloVideo.isOpened():
        print("Could not open video capture")
        exit()

    # Scale down
    scale = 3

    # Read the first frame to get its size
    ret, frame = telloVideo.read()
    if not ret:
        print("Could not read first frame")
        exit()

    # Resize the image for improved performance
    height, width, layers = frame.shape
    new_h = int(height / scale)
    new_w = int(width / scale)
    resize = cv2.resize(frame, (new_w, new_h))

    # Loop until 'q' is pressed
    while True:
        # Capture frame-by-frame
        ret, frame = telloVideo.read()
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('Tello', resize)

            # Write the image to disk if 's' is pressed
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite("test.jpg", resize)
                print("Take Picture")

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the capture and close the window
cv2.destroyAllWindows()
