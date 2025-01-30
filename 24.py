n = int(input())
i = 2
p = []
q = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
for w in range(0, len(q)):
    for k in range(1, n + 1):
        if n % q[w] == 0:
            n = n // q[w]
            p.append(q[w])
if n > 1:
    p.append(n)
m = str(p[0])
for k in range(1, len(p)):
    m += ' * ' + str(p[k])
print(m)