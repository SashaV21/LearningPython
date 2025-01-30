days = int(input())

data = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

for i in range(days):
    print(data[i % 5])