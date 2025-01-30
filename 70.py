example = 'зайка'
ans = set()

while (pole := input().split()) != []:
    seen = None
    for item in pole:
        if seen == example:
            ans.add(item)
        if item == example:
            if seen:
                ans.add(seen)
        seen = item

for item in ans:
    print(item)