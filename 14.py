a = int(input())
b = int(input())

ab = a * b

while a != b:
    if a < b:
        b = b - a
    else:
        a = a - b
print(ab // a)
