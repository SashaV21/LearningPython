def find_max_num(data):
    max_num = 0
    num = 0
    while data > 0:
        num = data % 10
        max_num = max(num, max_num)
        data = data // 10
    return max_num


n = int(input())
ans = ''
for i in range(n):
    num = int(input())
    ans += str(find_max_num(num))
print(ans)