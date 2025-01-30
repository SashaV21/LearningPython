start = int(input())
end = int(input())
data = str()

for i in range(start, end + 1):
    data += str(i)
    if i != end:
        data += ' '
print(data)
