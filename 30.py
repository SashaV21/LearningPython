def sum_num(a):
    ans = 0
    while a > 0:
        ans += a % 10
        a = a // 10
    return ans


n = int(input())
pwd = 0
for i in range(n):
    pwd += sum_num(int(input()))
print(pwd)
