# Whack a Mole Project for Raspberry Pi

import RPi.GPIO as GPIO
import time

buttonpin = 37
ledpin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if GPIO.input(buttonpin) == GPIO.HIGH:
        GPIO.output(ledpin, GPIO.HIGH)
        
    else:
        GPIO.output(ledpin, GPIO.LOW)
        
        
    time.sleep(0.01)

GPIO.cleanup()


# Prototype Scrapped Version

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)


# GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(5, GPIO.OUT)
# GPIO.output(5, GPIO.LOW)
# while True:

#     if GPIO.input(40) == 0:
#         GPIO.output(5, GPIO.HIGH)
#         print("button pressed")

#     else:
#         GPIO.output(5, GPIO.LOW)
#         print("button released")
#     time.sleep(2)

#     # GPIO.output(5, GPIO.LOW)
#     # while GPIO.input(40) == 0:
#     #     print("button pressed")
#     #     time.sleep(0.2)

#     # GPIO.output(5, GPIO.HIGH)
#     # while GPIO.input(40) == 1:
#     #     print("button released")
#     #     time.sleep(0.2)
# GPIO.cleanup()
