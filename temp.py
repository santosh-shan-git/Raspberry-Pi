# Temperature Sensor Project

#setting up DHT library, time and GPIO system
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
GPIO.setmode(GPIO.BOARD)

#defining variables
sensordht = Adafruit_DHT.DHT22
pindht = 7
GPIO.setup(pindht, GPIO.OUT)

while True:
    #defining humidity and temperature variables
    humidity, temperature = Adafruit_DHT.read(sensordht, pindht)

    #checking to see if it worked

    if humidity is not None and temperature is not None:
        #puts temp and humidity onto screen
        print("Temp={0:0.1f}C   Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        #tells us to check our wiring again
        print("Sensor Failure. Check Wiring.")
        
    time.sleep(3)
