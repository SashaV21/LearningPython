def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


n = int(input())
ans = 1
last_num = 1
for i in range(n):
    num = int(input())
    ans = GCD(last_num, num)
    last_num = num

print(ans)
