# для простоты создадим собственные данные, которые включают
# 100000 строк рандомных значений

# импортируем необходимые библиотеки
import numpy

# заголовки столбцов и данные для заполнения
columns=['January', 'February', 'March', 'April','May','June ','July','August','September','October',
         'November','December','men','wemen','num']
data = numpy.random.randint(1000, size=(100000, len(columns)))

# создаем *.csv файл с необходимыми данными
# df = pd.DataFrame(data, columns=columns)
# df.to_csv(r'data.csv')