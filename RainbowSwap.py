from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

while True:
        
    for i in range(0,8):
        for j in range(0,8):
            sense.set_pixel(i,j,(randint(0,150),randint(0,150),randint(0,150)))
            sleep(0.01)
