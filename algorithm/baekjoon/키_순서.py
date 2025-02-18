def abc(x):
    if len(path) == N-1:
        return
    for i in arr[x]:
        if i not in path:
            path.append(i)
            abc(i)

def bbq(x):
    if len(path) == N-1:
        return
    for i in arr2[x]:
        if i not in path:
            path.append(i)
            bbq(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
arr2 = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)
    arr2[a].append(b)

student = 0

for i in range(N, 0, -1):
    path = []
    abc(i)
    bbq(i)
    if len(path) == N-1:
        student += 1

print(student)