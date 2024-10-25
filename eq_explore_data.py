from pathlib import Path
import json
import plotly.express as px
import pandas as pd

#将数据集作为字符串读取并转换为python对象
# path = Path('eq_data/eq_data_1_day_m1.json')
path = Path('eq_data/eq_data_30_day_m1.json')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf8')

all_eq_data = json.loads(contents)

# #将数据文件转换为更易于阅读的版本
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

#查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(titles[:10])
# print(lons[:10])
# print(lats[:10])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags),
    columns=['Longitude', 'Latitude', 'position', 'magnitude']
)

fig = px.scatter(
    data,
    x='Longitude',
    y='Latitude',
    range_x=[-200, 200],
    range_y=[-100, 100],
    width=800,
    height=800,
    title='全球地震散点图',
    size='magnitude',
    size_max=10,
    color='magnitude',
    hover_name='position',
)
fig.show()