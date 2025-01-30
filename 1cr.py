_ = int(input())
nums = dict()
data = [int(x) for x in input().split()]

for num in data:
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1

count = 0
for num in nums:
    if nums[num] == 1:
        count += 1
print(count)

