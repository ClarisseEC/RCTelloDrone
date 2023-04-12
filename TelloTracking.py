# Import necessary libraries
from djitellopy import Tello
import cv2

# Connect to Tello drone
tello = Tello()
tello.connect()
tello.streamon()

# Define the tracker type (e.g. CSRT, KCF, MOSSE, etc.)
tracker_type = "CSRT"

# Create a OpenCV tracker object
tracker = cv2.TrackerCSRT_create() if tracker_type == "CSRT" else cv2.TrackerKCF_create()

# Define the bounding box coordinates of the object to be tracked (x, y, w, h)
bbox = (100, 100, 200, 200)

# Initialize the OpenCV tracker with the first frame and the bounding box
frame = tello.get_frame_read().frame
ok = tracker.init(frame, bbox)

# Loop through the frames
while True:
    # Get the next frame from the Tello drone
    frame = tello.get_frame_read().frame

    # Update the tracker with the current frame
    ok, bbox = tracker.update(frame)

    # Draw the bounding box around the tracked object
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # Display the resulting frame
    cv2.imshow("Object Tracking", frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
tello.streamoff()
cv2.destroyAllWindows()
