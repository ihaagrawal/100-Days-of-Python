# with open('.\\weather_data.csv','r') as weather_data:
#     data=weather_data.readlines()
#     print(data)

# import csv
# with open('.\\weather_data.csv','r') as weather_data:
#     data=csv.reader(weather_data)
#     temperature=[]
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)



import pandas as pd
df=pd.read_csv('weather_data.csv')
print(df['temp'].mean().round(2))
print(df['temp'].max())
print(df[df['temp']==df['temp'].max()])

monday_temp=int(df['temp'][df['day']=='Monday'])
print(monday_temp)
print((monday_temp*(9/5))+32)