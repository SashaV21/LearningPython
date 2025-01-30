num = int(input())
first_number = num // 100
third_number = num % 10
second_nuber = num // 10 % 10
max_num = max(first_number, second_nuber, third_number)
min_num = min(first_number, second_nuber, third_number)
if max_num + min_num == (first_number + second_nuber + third_number - max_num - min_num) * 2:
    print("YES")
else:
    print("NO")