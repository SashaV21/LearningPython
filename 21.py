n = int(input())
count = 0
for i in range(n):
    msg = str(input())
    if "зайка" in msg:
        count += 1
print(count)
