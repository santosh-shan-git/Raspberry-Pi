#Code for Controlling Car
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#motor1(red and blue wires)
in1=16
in2=12

#motor2(green and yellow wires)
in3=10
in4=8

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# GPIO.output(in1, 0)
# p=GPIO.PWM(in2, 50)
# p.start(50)
# time.sleep(10)
# p.stop()
GPIO.output(in1, 1)
GPIO.output(in2, 0)
GPIO.output(in4, 0)
GPIO.output(in3, 1)
time.sleep(60)
GPIO.output(in1, 0)
GPIO.output(in2, 0)
GPIO.output(in3, 0)
GPIO.output(in4, 0)
