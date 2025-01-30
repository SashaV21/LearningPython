def find_pol(num):
    half = 0
    if num < 0 or (num != 0 and num % 10 == 0):
        return 0
    while num > half:
        half = (half * 10) + num % 10
        num = num // 10
    return 1 if (num == half or num == half // 10) else 0


size = int(input())
ans = 0
for i in range(size):
    ans += find_pol(int(input()))
print(ans)
