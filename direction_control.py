# Date: 2025-09-23
# Author: Xia Dongxu
# Student ID: 202283890007
# Description: This script controls the robot to move in multiple directions, including forward, backward, left, right, spin left, and spin right.

from microbit import display, Image, sleep
import tinybit

# Define movement patterns with their corresponding actions, speed, display arrows, and durations
MOVEMENTS = [
    (tinybit.car_run, 150, Image.ARROW_S, 1000),       # Forward
    (tinybit.car_back, 150, Image.ARROW_N, 1000),      # Backward
    (tinybit.car_left, 150, Image.ARROW_E, 1000),      # Left
    (tinybit.car_right, 150, Image.ARROW_W, 1000),     # Right
    (tinybit.car_spinleft, 150, Image.ARROW_E, 1000),  # Spin left
    (tinybit.car_spinright, 150, Image.ARROW_W, 1000)  # Spin right
]

# Main loop to continuously cycle through the movements
while True:
    for move_func, speed, arrow, duration in MOVEMENTS:
        move_func(speed)          # Execute movement
        display.show(arrow)       # Show corresponding arrow on the micro:bit display
        sleep(duration)           # Wait for the specified duration

    # Stop between movement sequences
    tinybit.car_stop()             # Stop the car after a full cycle
    display.clear()                # Clear the display
    sleep(1000)                    # Pause before starting the next cycle
