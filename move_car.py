# Date: 2025-09-23
# Author: Xia Dongxu
# Student ID: 202283890007
# Description: This script is designed to control a TinyBit car using Micro:bit.
# It shows an arrow indicating forward movement, runs the car for 2 seconds at speed 150, and then stops it.

import tinybit
from microbit import display, Image, sleep

# Display an arrow indicating forward movement
display.show(Image.ARROW_S)

# Move the TinyBit car forward at speed 150.
tinybit.car_run(150)

# Pause the execution of the program for 2 seconds.
sleep(2000)

# Stop the TinyBit car after the specified duration has elapsed.
tinybit.car_stop()
