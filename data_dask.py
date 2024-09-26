# импортируем библиотеки
import dask.dataframe as dd
import datetime

# данные одного файла
DATASET = 'data/part-00000-aba60f69-2b63-4cc1-95ca-542598094698-c000.snappy.parquet'

# данные датасета
# DATASET = 'data'

# время старта расчета
start = datetime.datetime.now()
# чтение датасета
df = dd.read_parquet(DATASET)
# вывод первых 20 заголовков
print(df.url_host.str.split('\.').head(20))
# вывод и группировка
print(df.groupby('cpe_model_os_type').cpe_model_os_type.count().compute())

# время окончания расчета
finish = datetime.datetime.now()
# вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))
