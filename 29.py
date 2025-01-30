number = int(input())
prev_len = 0
lenght = 0
end_str = ' '
for i in range(1, number + 1):
    lenght += 1
    end_str = ' '
    if lenght == prev_len + 1:
        end_str = '\n'
        prev_len += 1
        lenght = 0
    print(i, end=end_str)
