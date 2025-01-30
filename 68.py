n = int(input())  # кол-во продукутов

menu = dict()
food = set()
ans = []
for _ in range(n):
    food.add(input())

num_of_eat = int(input())

for _ in range(num_of_eat):
    name = input()
    num_of_food = int(input())
    for __ in range(num_of_food):
        if name not in menu:
            menu[name] = {input()}
        else:
            menu[name].add(input())

for eat in sorted(menu):
    if menu[eat] <= food:
        ans.append(eat)

if len(ans) > 0:
    print('\n'.join(ans))
else:
    print("Готовить нечего")