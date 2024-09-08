from machine import Pin
import utime
from picozero import Speaker
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
speaker = Speaker(15)
myLED = Pin(14,Pin.OUT)
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
   
   if distance < 62:
       print("TOO CLOSE")
       myLED.value(1)
       speaker.play('c7', 0.01)
       utime.sleep(0.01)
       speaker.play('c6', 0.01)
       utime.sleep(0.01)
       speaker.play('c5', 0.01)
       utime.sleep(0.01)
       speaker.play('c4', 0.01)
       utime.sleep(1)
       myLED.value(0)
while True:
   ultra()
   utime.sleep(2)