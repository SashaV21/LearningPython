h = int(input())
w = int(input())

cell_w = len(str(h * w))

for i in range(1, h + 1):
    for j in range(w * (i - 1) + 1, w * i + 1):
        print(f'{i:<{cell_w}}', end=' ')
        if j == w * i:
            print()