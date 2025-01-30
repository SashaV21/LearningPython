while string := input():
    if not (pos := string.find('#')) + 1:
        print(string)
    elif string[:pos]:
        print(string[:pos])
