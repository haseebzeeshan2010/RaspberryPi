from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()


pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

print(f"temperature: {temperature}" )
print(f"humidity: {humidity}")
print(f"pressure: {pressure} ")




