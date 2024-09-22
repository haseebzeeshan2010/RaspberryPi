from machine import Pin
from picozero import Speaker
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
speaker = Speaker(4)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   return distance

while True:
   if ultra() < 55:
       speaker.play('c7', 0.5)
   utime.sleep(1)
   