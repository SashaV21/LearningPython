from itertools import accumulate

data = input().split()
for i in range(len(data) - 1):
    data[i] += ' '

for value in accumulate(data):
    print(value)

