num = int(input())

num_list = list(str(num))
num_list = [int(x) for x in num_list]

num_list.sort()

if num_list[0] == 0:
    print(num_list[1] * 10 + num_list[0], num_list[2] * 10 + num_list[1])
else:
    print(num_list[0] * 10 + num_list[1], num_list[-1] * 10 + num_list[1])