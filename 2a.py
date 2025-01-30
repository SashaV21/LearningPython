num = int(input())
max_ = num
count = 1
while num != 0:
    num = int(input())
    if num == max_:
        count += 1
    elif max_ < num:
        max_ = num
        count = 1
print(count)