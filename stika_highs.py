from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2014.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

# for index,column_header in enumerate(header_row):
#     print(index, column_header)

#提取最高温度
highs=[]
for row in reader:
    high=int(row[2])
    highs.append(high)

print(highs)
