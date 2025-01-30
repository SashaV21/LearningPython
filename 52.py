data = [int(x) for x in input().split()]
degree = int(input())
data = [x ** degree for x in data]
print(' '.join(str(item) for item in data))