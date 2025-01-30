n = int(input())
data = list(map(int, input().split()))

data.sort()
book = dict()
for i in range(n):
    if data[i] not in book:
        book[data[i]] = 1
    else:
        book[data[i]] += 1


max_name = -10000
max_count = -10000

for name in sorted(book):
    if max_count <= book[name] and max_name < name:
        max_name = name
        max_count = book[name]

print(max_name)

