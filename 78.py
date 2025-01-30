rle = [('a', 2), ('b', 3), ('c', 1)]

chars = []

for char, count in rle:
    chars.append(char * count)

result = ''.join(chars)

print(''.join([char * count for char, count in rle]))