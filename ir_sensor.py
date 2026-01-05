
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
red=15
green=16
GPIO.setup(40, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.output(green, GPIO.LOW)
GPIO.output(red, GPIO.LOW)
while True:
    inp=GPIO.input(40)
    print(inp)
    if inp==0:
        GPIO.output(green, GPIO.HIGH)
        time.sleep(0.0005)
        GPIO.output(red, GPIO.LOW)
    if inp==1:
        GPIO.output(red, GPIO.HIGH)
        time.sleep(0.0005)
        GPIO.output(green, GPIO.LOW)
    

trig=5
echo=3
gnd=39
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
while True:
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.000001)
    GPIO.output(trig, GPIO.LOW)
    while GPIO.input(echo)==0:
        start=time.time()
    while GPIO.input(echo)==1:
        stop=time.time()
    difference=stop-start
    d=(34300 * difference) / 2
    print(d)
    time.sleep(1)