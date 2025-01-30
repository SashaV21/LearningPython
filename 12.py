pwd = 0.0
while (num := float(input())) != 0:
    if num >= 500:
        pwd += (num * 0.9)
    else:
        pwd += num
print(pwd)
