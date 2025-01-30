def operation(pwd: list, op: str):
    if op == "+":
        second_num = int(pwd.pop())
        first_num = int(pwd.pop())
        pwd.append(str(first_num + second_num))
    elif op == "-":
        second_num = int(pwd.pop())
        first_num = int(pwd.pop())
        pwd.append(str(first_num - second_num))
    elif op == "*":
        second_num = int(pwd.pop())
        first_num = int(pwd.pop())
        pwd.append(str(first_num * second_num))


_input = input().split()

data = []
for i in range(len(_input)):
    if _input[i] not in "+-*":
        data.append(_input[i])
    else:
        operation(data, _input[i])
        i += 1
print(data[0])

