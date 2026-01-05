# Ultrasonic Sensor for Raspberry Pi

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# s=33400
# trig=3
# echo=5
# bulb=40
# irinput=10
# GPIO.setup(10, GPIO.IN)
# GPIO.setup(trig,GPIO.OUT)
# GPIO.setup(echo,GPIO.IN)
# GPIO.setup(bulb, GPIO.OUT)
# GPIO.output(bulb, GPIO.LOW)
# while True:
#     val=GPIO.input(irinput)
#     if val==0:
#         GPIO.output(trig,GPIO.HIGH)
#         time.sleep(0.000001)
#         GPIO.output(trig,GPIO.LOW)
#         while GPIO.input(echo)==0:
#             start=time.time()
#         while GPIO.input(echo)==1:
#             stop=time.time()
#         t=stop-start
#         d=t * s
#         dd=d//2
#         print(dd)
#         time.sleep(0.1)
#         if dd <=3:
#             GPIO.output(bulb,GPIO.HIGH)
#         else:
#             GPIO.output(bulb,GPIO.LOW)

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# echo=36
# trig=38
# s=34300
# GPIO.setup(echo, GPIO.IN)
# GPIO.setup(trig, GPIO.OUT)

# while True:
#     GPIO.output(trig, 1)
#     time.sleep(0.001)
#     GPIO.output(trig, 0)

#     while GPIO.input(echo)==0:
#         start=time.time()

#     while GPIO.input(echo)==1:
#         stop=time.time()

#     t= stop - start
#     d= s * t
#     D= d / 2

#     print(D)
#     time.sleep(1)

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#fvolt=4
#gnd=25
echo=26
trig=24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

while True:

    GPIO.output(trig, 1)
    time.sleep(0.000001)
    GPIO.output(trig, 0)

    while GPIO.input(echo)==0:
        start=time.time()
    
    while GPIO.input(echo)==1:
        stop=time.time()

    t=stop - start
    c= 343000 * t
    d= c / 2
    print(d)
    time.sleep(1)
