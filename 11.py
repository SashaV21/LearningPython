start = int(input())
end = int(input())

data = str()

if start < end:
    for i in range(start, end + 1):
        data += str(i)
        if i != end:
            data += ' '

elif start > end:
    for i in range(start, end - 1, -1):
        data += str(i)
        if i != end:
            data += ' '
print(data)
