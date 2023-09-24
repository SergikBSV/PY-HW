import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

values_data = data['whoAmI'].unique()
one_hot = pd.DataFrame()

for value in values_data:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

one_hot[['robot', 'human']]