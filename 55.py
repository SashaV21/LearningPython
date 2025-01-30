string = "".join(input().split()).lower()
print("YES" if string == string[::-1] else "NO")
