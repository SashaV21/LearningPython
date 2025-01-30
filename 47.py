n = int(input())

for _ in range(n):
    position = input().find("зайка") + 1
    if position:
        print(position)
    else:
        print("Заек нет =(")


