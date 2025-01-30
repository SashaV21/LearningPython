list1size = int(input())
list2size = int(input())

list1 = set()
list2 = set()

for _ in range(list1size):
    list1.add(input())

for _ in range(list2size):
    list2.add(input())

if len(junction := (list1 & list2)) != 0:
    print(len(junction))
else:
    print('Таких нет')
