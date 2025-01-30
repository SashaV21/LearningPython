n = int(input())
data = list(map(int, input().split()))
data.sort()

"""data1 = []

for i in range(n):
    if data[i] > 1:
        data1.append(data[i] - 1)
    if data[i] == 1:
        data1.append(1)
"""
# data1.pop(0)

ans = sum(data[0])
print(ans)
