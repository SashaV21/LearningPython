n = int(input())
count = 0
for _ in range(n):
    line = input()
    count += line.count('зайка')
print(count)
