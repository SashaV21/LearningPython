def find_simple(n):
    flag = 1
    if n == 1:
        flag = 0
    else:
        i = 2
        while i <= n ** 0.5:
            if n % i == 0:
                flag = 0
                break
            i += 1
    return flag


n = int(input())
count = 0
for i in range(n):
    num = int(input())
    count += find_simple(num)
print(count)
