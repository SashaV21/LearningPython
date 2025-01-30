n = int(input())
name_min = "Яяяяяяяяяяя"

for i in range(n):
    name = str(input())
    if name < name_min:
        name_min = name

print(name_min)