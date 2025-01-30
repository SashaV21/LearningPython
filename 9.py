first_str = str(input())
second_str = str(input())
third_str = str(input())

data = ""
dl = 1000
example = "зайка"

if example in first_str:
    data = first_str
    dl = len(data)
if example in second_str and len(second_str) < dl:
    data = second_str
    dl = len(second_str)
if example in third_str and len(third_str) < dl:
    data = third_str
    dl = len(third_str)
print(f"{data} {dl}")