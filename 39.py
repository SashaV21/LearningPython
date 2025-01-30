h = int(input())
w = int(input())

size_of_h = len(str(h * w))

for i in range(1, h + 1):
    for j in range(i, i + h * (w - 1) + 1, h):
        print(f'{j:<{size_of_h}}', end=" ")
        if j == i + h * (w - 1):
            print()
