import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
unique_values = data['whoAmI'].unique()
new_data = pd.DataFrame()
for value in unique_values:
    new_data[value] = (data['whoAmI'] == value).astype(int)
new_data.head()
