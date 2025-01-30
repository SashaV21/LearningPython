"""
num = int(input())

num_pwd = num
count = 0

while num_pwd > 10:
    num_pwd = num_pwd // 10
    count += 1

finish = 0
num_pwd = num

while num_pwd > 0:
    finish += (num_pwd % 10) * (10 ** count)
    num_pwd = num_pwd // 10
    count -= 1

print("YES" if num == finish else "NO")
"""
x = int(input())
half = 0
if x < 0 or (x != 0 and x % 10 == 0):
    print("NO")
else:
    while x > half:
        half = (half * 10) + (x % 10)
        x = x // 10
    print("YES" if (x == half or x == half // 10) else "NO")
