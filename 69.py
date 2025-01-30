def count_num(a):
    units = 0
    zeros = 0
    for i in range(len(a)):
        if a[i] == '1':
            units += 1
        elif a[i] == '0':
            zeros += 1
    return units, zeros


nums = [format(int(x), 'b') for x in input().split()]
ans = []

for num in nums:
    info = dict()
    info["digits"] = len(num)
    info["units"], info["zeros"] = count_num(num)
    ans.append(info)

print(ans)
