import pandas as pd

df = pd.read_csv('Weather_Data.csv')
print(df['Humidity'][4:])