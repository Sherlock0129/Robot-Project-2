# Author: Xia Dongxu
# Student ID: 202283890007
# Date: 2025-09-23
# Description: This program demonstrates speed control of the TinyBit robot car.

from microbit import display, Image, sleep
import tinybit

# Show a happy face to indicate program start
display.show(Image.HAPPY)

# Define user-customizable speed levels (left speed, right speed, duration)
SPEED_PROFILES = [
    (0, 0, 1000),      # Stop
    (50, 50, 1000),    # Very slow
    (100, 100, 1000),  # Slow
    (150, 150, 1000),  # Medium speed
    (200, 200, 1000),  # Fast
    (255, 255, 1000),  # Full speed
]

# Main loop to execute the speed profiles in sequence
while True:
    for left_speed, right_speed, duration in SPEED_PROFILES:
        tinybit.car_run(left_speed, right_speed)  # Run car at the specified speed
        sleep(duration)  # Wait for the specified duration
        tinybit.car_stop()  # Stop the car after each speed profile
        sleep(1000)  # Wait 1 second before moving to the next speed profile
