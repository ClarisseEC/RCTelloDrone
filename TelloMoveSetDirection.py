from djitellopy import Tello

import cv2, math, time

tello = Tello()
tello.connect()

# print("Current Battery Life: " + int(tello.get_battery()))

tello.takeoff()



# move in circle
tello.move_forward(50)
tello.rotate_counter_clockwise(90)

tello.move_forward(50)
tello.rotate_counter_clockwise(90)

tello.move_forward(50)
tello.rotate_counter_clockwise(90)

tello.move_forward(25)
tello.rotate_counter_clockwise(90)

# back to start
tello.move_forward(25)
tello.land()