
# импортируем необходимые библиотеки
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
# ---------------------------
# открываем файл
bdata = pd.read_csv('data.csv')

# -------------------------------
# количество строк
# print(bdata.shape)

# заголовки и первые 5 строк
# print(bdata.head())

# первые и последние 5 строк
# print(bdata)

# -------------------------------
# фильтрация значений
# bd1 = bdata[bdata['num'] > 900 ]
# print(bd1.shape)
# print(bd1.head())

# выводим необходимые строки и столбцы
# bd2 = bdata.loc[15:19, ['July']]
# print(bd2)

# еще один способ фильтрации по многим признакам
# bd3 = bdata.query('July > 400 & men < 600 & num > 700')
# print(bd3.shape)
# print(bd3.head())

# выводим необходимые строки и столбцы
# bd4 = bdata.iloc[:10, 2:6]
# print(bd4.shape)
# print(bd4.head())

# фильтрация с помощью маски и замена значений
mask = (50 < bdata) & (bdata < 1000)
bd_new =bdata.where(mask, None)
# print(bd_new)

# -------------------------------
# визуализация

# тепловая карта пропущенных значений
# cols = bd_new.columns[1:13] # первые 13 колонок
# определяем цвета
# colours = ['#000099', '#1aff12']# зеленый - пропущенные данные, синий - не пропущенные
# sns.heatmap(bd_new[cols].isnull(), cmap=sns.color_palette(colours))
# plt.show()
# таблица с пропущенными значениями
# for col in bd_new.columns:
#     pct_missing = np.mean(bd_new[col].isnull())
#     print('{} - {}%'.format(col, round(pct_missing*100)))



# Вывод таблицы с пропущенными значениями
for col in bd_new.columns:
    missing = bd_new[col].isnull()
    num_missing = np.sum(missing)

missing_table = bd_new.isnull().sum().reset_index()
missing_table.columns = ['month', 'num_missing']
#
y=list(missing_table['num_missing'])[1:]
x=list(missing_table['month'])[1:13]
#
missing_table['num_missing'][1:].plot(kind="bar", fontsize=10)
missing_table['num_missing'][1:].plot(color='red')


#построение гистограммы  с пропущенными значениями
# missing_table['num_missing'][1:].plot(kind="pie", ylabel='Total clicks', fontsize=8)
# fig, axes = plt.subplots(2, 1)
# data = pd.Series(y)
# data.plot.bar(ax=axes[0], color='k', alpha=0.7) # вертикальная
# data.plot.barh(ax=axes[1], color='k', alpha=0.7) # горизонтальная
# plt.show()


#построение кольцевой гистограммы
z1,z2,z3 = sum(bdata['January']),sum(bdata['February']),sum(bdata['December'])
v1,v2,v3 = sum(bdata['March']),sum(bdata['April']),sum(bdata['May'])
l1,l2,l3 = sum(bdata['June ']), sum(bdata['July']), sum(bdata['August'])
o1,o2,o3 = sum(bdata['September']), sum(bdata['October']), sum(bdata['November'])

fig, ax = plt.subplots()
offset=0.4
data = np.array([[z1, z2, z3], [v1, v2, v3], [l1, l2, l3], [o1, o2, o3]])
cmap = plt.get_cmap("tab20b")
b_colors = cmap(np.array([0, 8, 12]))
sm_colors = cmap(np.array([1, 2, 3, 9, 10, 11, 13, 14, 15]))
ax.pie(data.sum(axis=1), radius=1, colors=b_colors, wedgeprops=dict(width=offset, edgecolor='w'))
ax.pie(data.flatten(), labels=x, autopct='%1.1f%%', radius=1-offset, colors=sm_colors, wedgeprops=dict(width=offset, edgecolor='w'))
plt.show()