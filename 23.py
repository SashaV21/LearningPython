num = list(str(input()))
num = [int(x) for x in num]
final_num = ''
for i in range(len(num)):
    if num[i] % 2 != 0:
        final_num += str(num[i])

print(final_num)
