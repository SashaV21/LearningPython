size = int(input())
n = int(input())

for _ in range(n):
    headline = input()
    if len(headline) <= size:
        print(headline)
    else:
        print(headline[:size - 3] + "...")