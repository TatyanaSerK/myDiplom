# импортируем необходимые библиотеки
import dask.dataframe as dd
import dask.array as da
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# ---------------------------
# открываем файл
df = dd.read_csv('data.csv')

# ---------------------------
# количество строк
# n_rows = df.shape[0].compute()

# количество столбцов
# print(n_rows)

# заголовки и первые 5 строк
# print(df.head())

# последние 5 строк
# print(df.tail())

# ---------------------------
# Фильтрация данных:
df_filtered = df.loc[df['men'] > 300]
# print(df_filtered.head())
# print(df_filtered.tail())

# ---------------------------
# операции над данными:
# Расчет среднего значения столбца
mean_value = df['July'].mean()
# Вычисление результата и вывод
result = mean_value.compute()
# print(result)

# Преобразование столбца 'age' в числовой тип данных
df['num'] = df['num'].astype(float)
print(df.head())

# Создание нового столбца 'income_per_age'
df['income_per_age'] = df['men'] / df['num']
print(df.head())

# -------------------------------
# визуализация

# fig = plt.figure(figsize=(6, 4))
# ax = fig.add_subplot()
# #построение кольцевой гистограммы
z1,z2,z3 = sum(df['January']),sum(df['February']),sum(df['December'])
v1,v2,v3 = sum(df['March']),sum(df['April']),sum(df['May'])
l1,l2,l3 = sum(df['June ']), sum(df['July']), sum(df['August'])
o1,o2,o3 = sum(df['September']), sum(df['October']), sum(df['November'])
# offset=0.4
# x = ['z', 'v', 'l', 'o']
# y = np.array([[z1, z2, z3], [v1, v2, v3], [l1, l2, l3], [o1, o2, o3]])
# cmap = plt.get_cmap("tab20b")
# b_colors = cmap(np.array([0, 8, 12]))
# sm_colors = cmap(np.array([1, 2, 3, 9, 10, 11, 13, 14, 15]))
# ax.pie(y.sum(axis=1), radius=1, colors=b_colors, wedgeprops=dict(width=offset, edgecolor='w'))
# ax.pie(y.flatten(), autopct='%1.1f%%', radius=1-offset, colors=sm_colors, wedgeprops=dict(width=offset, edgecolor='w'))
# plt.show()

# y=list(df['num'])[70:100]
y1=(z1, z2, z3, v1, v2, v3, l1, l2, l3, o1, o2, o3 )
fig, axes = plt.subplots(2, 1)
data = pd.Series(y1)
data.plot.bar(ax=axes[0], color='k', alpha=0.7) # вертикальная
data.plot.barh(ax=axes[1], color='k', alpha=0.7) # горизонтальная
plt.show()