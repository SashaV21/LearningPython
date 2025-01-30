def sum_of_num(a):
    s = 0
    while a > 0:
        s += a % 10
        a = a // 10
    return s


n = int(input())

last_name = ''
max_num = 0
for i in range(n):
    name = input()
    num = int(input())
    if sum_of_num(num) >= max_num:
        max_num = sum_of_num(num)
        last_name = name
print(last_name)
