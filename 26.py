last_hash = 0
for i in range(int(input())):
    block = int(input())
    now_hash = block % 256
    r = block // 256 % 256
    m = block // 256 ** 2
    count_hash = 37 * (m + r + last_hash) % 256
    if count_hash != now_hash or now_hash >= 100:
        print(i)
        break
    last_hash = now_hash
else:
    print(-1)
