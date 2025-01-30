def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


data = [int(x) for x in input().split()]
last_ans = data[0]
for i in range(1, len(data)):
    last_ans = gcd(last_ans, data[i])
print(last_ans)
