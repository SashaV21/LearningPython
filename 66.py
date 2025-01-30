num = int(input())

female = dict()

for i in range(num):
    name = input()
    if name not in female:
        female[name] = 1
    else:
        female[name] += 1
flag = 1
for name in sorted(female):
    if female[name] > 1:
        print(f'{name} - {female[name]}')
        flag = 0
if flag == 1:
    print("Однофамильцев нет")




