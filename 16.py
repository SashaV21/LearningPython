x = 0
y = 0

while (direct := input()) != "СТОП":
    num = int(input())
    if direct == "СЕВЕР":
        y += num
    elif direct == "ВОСТОК":
        x += num
    elif direct == "ЮГ":
        y -= num
    elif direct == "ЗАПАД":
        x -= num

print(y, x, sep='\n')
