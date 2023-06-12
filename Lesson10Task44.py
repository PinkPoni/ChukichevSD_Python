# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())


# Перевод в one hot вид с помощью метода pandas get_dummies
print(pd.get_dummies(data['whoAmI'])*1)


# Перевод в one hot вид без помощи метода pandas get_dummies
data.replace({'robot': 1, 'human': 0}, inplace = True)
data['human'] = data['whoAmI'].replace({0: 1, 1: 0})
data['robot'] = data['whoAmI']
data = data.drop(columns='whoAmI')
print(data)