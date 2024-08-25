# from sense_hat import SenseHat
# from random import randint
# from time import sleep
# from datetime import datetime
# import csv

# sense = SenseHat()
# sense.clear()

# while True:

# 	pressure = sense.get_pressure()
# 	temperature = sense.get_temperature()
# 	humidity = sense.get_humidity()


# 	for i in range(0,20):
# 		pressure += sense.get_pressure()
# 		humidity += sense.get_humidity()
# 		sleep(5)
# 		#sleep(1)

# 	pressure = pressure / 21
# 	humidity = humidity / 21

# 	print(f"temperature: {temperature}" )
# 	print(f"humidity: {humidity}")
# 	print(f"pressure: {pressure} ")
# 	print(f"date/time: {datetime.now()}")

# 	with open('Weather_Data.csv', mode='a') as weather_file:
# 		weather_writer = csv.writer(weather_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 		weather_writer.writerow([f"{datetime.now()}",f"{humidity}",f"{pressure}" "0"])
# 	sleep(1695)
	


from sense_hat import SenseHat
import time
from datetime import datetime
import csv
sense = SenseHat()
sense.clear()

while True:
	t = time.localtime()
	if t.tm_min in [0,15,30,45]:
		print("YES")
		current_time = datetime.now()
		
		pressure = sense.get_pressure()
		humidity = sense.get_humidity()


		for i in range(0,20):
			pressure += sense.get_pressure()
			humidity += sense.get_humidity()
			time.sleep(5)
			#sleep(1)

		pressure = pressure / 21
		humidity = humidity / 21


		print(f"p: {pressure} h: {humidity}")
		with open('Weather_Data.csv', mode='a') as weather_file:
			weather_writer = csv.writer(weather_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			weather_writer.writerow([f"{current_time}",f"{humidity}",f"{pressure}"])