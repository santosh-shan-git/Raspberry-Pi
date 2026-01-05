# Basics of Stepper Motor for Raspberry Pi

# # fivevolt=2
# # ground=6
# #if you replace the 0s w/ 1s and the 1s w/ 0s, the motor will reverse
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# onein=8
# twoin=29
# threein=31
# fourin=33
#
# GPIO.setup(onein, GPIO.OUT)
# GPIO.setup(twoin, GPIO.OUT)
# GPIO.setup(threein, GPIO.OUT)
# GPIO.setup(fourin, GPIO.OUT)
#
# lst=[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
#
# while True:
#     for step in lst:
#         GPIO.output(onein, step[0])
#         GPIO.output(twoin, step[1])
#         GPIO.output(threein, step[2])
#         GPIO.output(fourin, step[3])
#         time.sleep(0.002)

# #full_stepping
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# in1=22
# in2=24
# in3=26
# in4=32

# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(in3, GPIO.OUT)
# GPIO.setup(in4, GPIO.OUT)

# dualsteplst=[[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]

# while True:
#     for v in dualsteplst:
#         GPIO.output(in1, v[0])
#         GPIO.output(in2, v[1])
#         GPIO.output(in3, v[2])
#         GPIO.output(in4, v[3])
#         time.sleep(0.002)


# fivevolt=2
# ground=6
#if you replace the 0s w/ 1s and the 1s w/ 0s, the motor will reverse
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
in1=8
in2=10
in3=11
in4=12
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

lst=[[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]

while True:
    for v in lst:
        GPIO.output(in1, v[0])
        GPIO.output(in2, v[1])
        GPIO.output(in3, v[2])
        GPIO.output(in4, v[3])
        time.sleep(0.003)