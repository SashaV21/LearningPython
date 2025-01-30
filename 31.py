n = int(input())
s = 0
for i in range(1, n + 1):
    name = ''
    k = 0
    while name != 'ВСЁ':
        name = input()
        if name == 'зайка':
            k += 1
    s += k > 0
print(s)
