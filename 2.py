first = int(input())
second = int(input())
third = int(input())

if first + second > third and first + third > second and second + third > first:
    print("YES")
else:
    print("NO")