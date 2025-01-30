graph = dict()
ans = dict()

while (name := input().split()) != []:
    if name[0] not in graph:
        graph[name[0]] = {name[1]}
    else:
        graph[name[0]].add(name[1])
    if name[1] not in graph:
        graph[name[1]] = {name[0]}
    else:
        graph[name[1]].add(name[0])

for name in graph:
    for item in graph[name]:
        if name not in ans:
            ans[name] = set(graph[item])
            ans[name].discard(name)
        else:
            for k in graph[item]:
                if k != name:
                    ans[name].add(k)

# если в списке есть друзья первого уровня - удалить
for name in ans:
    ans[name] -= graph[name]

for item in sorted(ans):
    print(f'{item}:', end=' ')
    print(*sorted(ans[item]), sep=", ")
