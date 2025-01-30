treasures = dict()

for _ in range(count := int(input())):
    x, y = input().split()
    index = (int(x) // 10, int(y) // 10)
    treasures[index] = treasures.get(index, 0) + 1

print(max(treasures.values()))