data = input()
count = 0
for i in range(len(data) // 2):
    if data[i] != data[len(data) - i - 1]:
        count += 1
print(count)