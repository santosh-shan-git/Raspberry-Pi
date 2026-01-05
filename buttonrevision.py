# Code to Make Button Work on Raspberry Pi
ground=6
out=8
inp=10
gpio=12
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out, GPIO.OUT)
GPIO.setup(inp, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gpio, GPIO.OUT)

count=0

state=0

GPIO.output(out, GPIO.LOW)
while True:
    GPIO.output(out, GPIO.HIGH)
    # print(GPIO.input(inp))
    while GPIO.input(inp)==1:
        pass
    count=count+1
    print(count)

    while GPIO.input(inp)==0:
        pass
   

        

