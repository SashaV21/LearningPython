n = int(input())

msg = "YES"

if n == 1:
    msg = "NO"
else:
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            msg = "NO"
            break
        i += 1

print(msg)