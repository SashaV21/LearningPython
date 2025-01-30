height = int(input())
width = int(input())

ceil_width = len(str(width * height))

if height > 0 and width > 0:
    for row in range(height):
        for column in range(width):
            if (row % 2) == 0:
                num = row * width + column + 1
            else:
                num = (row + 1) * width - column
            print(f'{num:>{ceil_width}}', end=' ')
        print()