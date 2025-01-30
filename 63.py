num_of_people = int(input())
kind = dict()

for _ in range(num_of_people):
    data = input().split()
    female = data[0]
    for i in range(1, len(data)):
        eat = data[i]
        if eat not in kind:
            kind[eat] = [female]
        else:
            kind[eat].append(female)

nominal = input()
if nominal not in kind:
    print("Таких нет")
else:
    for fam in sorted(kind[nominal]):
        print(fam)
