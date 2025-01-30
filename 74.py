def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


table = dict()
data = [int(x) for x in input().split("; ")]
for num in data:
    table[num] = set()
    for opponent in data:
        if gcd(num, opponent) == 1:
            table[num].add(opponent)

for item in sorted(table):
    if table[item] == set():
        continue
    print(f'{item} - ', end='')
    print(*sorted(table[item]), sep=', ')
