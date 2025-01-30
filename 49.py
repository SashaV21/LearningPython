n = int(input())
data = []
for i in range(n):
    data.append(input())
find = input().lower()
count = 0
pwd = tuple(data)
data = [x.lower() for x in data]
for i, string in enumerate(data):
    if find in string:
        count += 1
        print(pwd[i])

