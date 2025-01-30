def factorial(a):
    res = 1
    while a > 0:
        res = res * a
        a -= 1
    return res


symbols = input().split()
stack = []

while symbols != []:
    value = symbols.pop(0)
    if value.isdigit():
        stack.append(int(value))
    else:
        match value:
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "-":
                stack.append(stack.pop(-2) - stack.pop())
            case "*":
                stack.append(stack.pop() * stack.pop())
            case "/":
                stack.append(stack.pop(-2) // stack.pop())
            case "~":
                stack.append(stack.pop() * (-1))
            case "!":
                stack.append(factorial(stack.pop()))
            case "#":
                stack.append(stack[-1])
            case "@":
                first_num = stack.pop(-3)
                second_num = stack.pop(-2)
                third_num = stack.pop()
                stack.append(second_num)
                stack.append(third_num)
                stack.append(first_num)

print(stack[0])
