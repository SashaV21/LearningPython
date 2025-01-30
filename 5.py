f_num = list(input())
s_num = list(input())

f_num = [int(x) for x in f_num]
s_num = [int(x) for x in s_num]

data = f_num + s_num
data.sort()

third = data[0]
data.pop(0)
first = data[-1]
data.pop(-1)
second = sum(data) % 10
print(first * 100 + second * 10 + third)
