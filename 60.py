n = int(input())
data = set()
for i in range(n):
    for elements in input().split():
        data.add(elements)

print("\n".join(data))