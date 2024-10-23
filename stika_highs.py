from cProfile import label
from pathlib import Path
import csv
import matplotlib.pyplot as plt

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

#根据最高温度绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

#设置绘图的格式
ax.set_title('Daily High Temperatures', fontsize=24)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
