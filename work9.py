'''
Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

Задача 42: Узнать какая максимальная households в зоне минимального значения population.
'''

import pandas as pd

data = pd.read_csv('california_housing_train.csv')

print(data[(data['population'] < 500) & (data['population'] > 0)][['population', 'median_house_value']])
print(data[data["population"] == data["population"].min()]["households"].max())