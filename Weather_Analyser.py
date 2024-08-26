import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Weather_Data.csv')
print(df['Humidity'])
print(df['Pressure'][:8])

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(df['Date/Time'], df['Pressure'])  # Plot some data on the Axes.
plt.show()