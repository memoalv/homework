import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

class dht22:

    def __init__(self, pin=17):
        self.tempSensorPin = pin
        self.tempSensor = Adafruit_DHT.DHT22

    def read(self):
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(
            self.tempSensor, self.tempSensorPin)
        return (humidity, temperature)