from itertools import count

a, b, c = map(float, input().split())

for value in count(a, c):
    if value <= b:
        print(f'{round(value, 10):.2f}')
    else:
        break
