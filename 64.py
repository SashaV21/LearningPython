animals = dict()

while (pol := input()) != '':
    pol = pol.split()
    for animal in pol:
        if animal not in animals:
            animals[animal] = 1
        else:
            animals[animal] += 1

for animal in animals:
    print(f'{animal} {animals[animal]}')