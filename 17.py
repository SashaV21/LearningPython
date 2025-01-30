num = int(input())
pwd = 0

while num > 0:
    pwd += (num % 10)
    num = num // 10

print(pwd)