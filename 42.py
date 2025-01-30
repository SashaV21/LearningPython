n = int(input())
litter = "абв"
flag = 0
for i in range(n):
    if input()[0] in litter:
        pass
    else:
        flag = 1
print("YES" if flag == 0 else "NO")