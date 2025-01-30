numbers = [3, 1, 2, 3, 2, 2, 1]

nums = []

for number in sorted(set(numbers)):
    nums.append(str(number))

result = ' - '.join(nums)

print(' - '.join([str(number) for number in sorted(set(numbers))]))