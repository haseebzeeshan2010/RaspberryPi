from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()


pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

for i in range(0,20):
    pressure += sense.get_pressure()
    humidity += sense.get_humidity()
    sleep(1)
    print(f"press: {pressure}  humid: {humidity}")

pressure = pressure / 21
humidity = humidity / 21


print(f"temperature: {temperature}" )
print(f"humidity: {humidity}")
print(f"pressure: {pressure} ")




