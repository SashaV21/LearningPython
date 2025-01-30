n = int(input())  # кол-во блюд, которые возможно приготовить

menu = dict()

# заполняем словарь видами блюд
for _ in range(n):
    eat = input()
    menu[eat] = 0

m = int(input())  # кол-во дней о которых есть информация

for _ in range(m):
    k = int(input())  # кол_во блюд приготовленных в конкретный день
    for __ in range(k):
        eat = input()
        menu[eat] += 1

flag = 0
for eat in sorted(menu):
    if menu[eat] == 0:
        print(eat)
        flag = 1
if flag == 0:
    print("Готовить нечего")