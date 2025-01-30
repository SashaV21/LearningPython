a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a >= b and a >= c:
        if a ** 2 > b ** 2 + c ** 2:
            print("велика")
        elif a ** 2 == b ** 2 + c ** 2:
            print("100%")
        else:
            print("крайне мала")
    if b > a and b >= c:
        if b ** 2 > a ** 2 + c ** 2:
            print("велика")
        elif b ** 2 == a ** 2 + c ** 2:
            print("100%")
        else:
            print("крайне мала")
    if c > a and c > b:
        if c ** 2 > a ** 2 + b ** 2:
            print("велика")
        elif c ** 2 == a ** 2 + b ** 2:
            print("100%")
        else:
            print("крайне мала")