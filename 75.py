numbers = {1, 2, 3, 4, 5, 6, 7, 8}
print({number: [divider for divider in range(1, number + 1) if number % divider == 0] for number in numbersx})

