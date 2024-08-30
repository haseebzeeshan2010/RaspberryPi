import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pressure_trend = 0

df = pd.read_csv('Weather_Data.csv')
# print(df['Humidity'])
# print(df['Pressure'][:8])

for i in range(0,len(df['Pressure'][:4]-1)):
    if df['Pressure'][i] < df['Pressure'][i+1]:
        pressure_trend += 1
    else:
        pressure_trend -= 1
    print(df['Pressure'][i])
    
print(f"Pressure trend = {pressure_trend}")
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(df['Date/Time'], df['Pressure'])  # Plot some data on the Axes.
plt.show()