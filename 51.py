count = int(input())
data = []

for i in range(count):
    data.append(int(input()))

degree = int(input())

for i in range(count):
    data[i] = data[i] ** degree
    print(data[i])