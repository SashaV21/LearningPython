data = [int(x) for x in input().split()]
data1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
data2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

count = 15
data3 = []
for i in range(10):
    if data[i] == 2:
        count = 0
        data1[i] = 0
    else:
        count += 1
        data1[i] = count

count = 15

for i in range(9, -1, -1):
    if data[i] == 2:
        count = 0
        data2[i] = count
    else:
        count += 1
        data2[i] = count

for i in range(10):
    if data[i] == 1:
        data3.append(min(data1[i], data2[i]))

print(max(data3))