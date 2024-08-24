import pandas as pd

df = pd.read_csv('Weather_Data.csv')
print(df['Humidity'][:8])
print(df['Pressure'][:8])