import pandas as pd

df=pd.read_csv('.\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color=df['Primary Fur Color'].value_counts()
color_count=pd.DataFrame(fur_color)
color_count.to_csv('color_count.csv')
color=pd.read_csv('color_count.csv')
print(color)
