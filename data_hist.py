#установка необходимых библиотек

from matplotlib import pyplot as plt

#построение столбчатой диаграммы
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()

#данные для построения
x = ['Pandas', 'Dask', 'Spark']
y1 = (0, 5.65, 05.65)
y2 = (33.87, 17.04, 34.16)
ax.bar(x, y2)
ax.bar(x, y1)

plt.show()