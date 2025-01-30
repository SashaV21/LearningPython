import itertools

data_1 = input().split(', ')
data_2 = input().split(', ')

data = list(zip(data_1, data_2))
for pairs in data:
    print(f'{pairs[0]} - {pairs[1]}')
