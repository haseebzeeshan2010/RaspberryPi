from machine import Pin
import time
import dht 

dSensor = dht.DHT22(Pin(2))

def readDHT():
    try:
        dSensor.measure()
        temp = dSensor.temperature()

        hum = dSensor.humidity()
        print(f'Temperature= {temp}')
        print(f'Humidity= {hum} ')
    except OSError as e:
        print('Failed to read data from DHT sensor')
    
while True:
    readDHT()
    time.sleep(5)
