string = 'открытое акционерное общество'
result = ''
chars = []

for word in string.split():
    chars.append(word[0].upper())
result = ''.join(chars)

print(''.join([word[0].upper() for word in string.split()]))
