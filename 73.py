
toys = []
unique = []

for _ in range(int(input())):
    name, string = input().split(': ')
    toys.extend(set(string.split(', ')))

for i in range(len(toys)):
    toy = toys.pop(0)
    if toy not in toys:
        unique.append(toy)
    toys.append(toy)

print('\n'.join(sorted(unique)))