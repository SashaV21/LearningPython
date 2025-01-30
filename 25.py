data = list()
while True:
    x = input()
    try:
        _ = int(x)
        break
    except ValueError:
        data.append(x)

x = int(x)
for i in range(10):
    num = int(input())
    if num < x:
        print("Больше")
    elif num > x:
        print("Меньше")
    else:
        print("Угадал!")
        break
