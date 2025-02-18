TC = int(input())

def dfs(level, now, total):
    global result

    if level == 1:
        result = max(result, total + now[0])
        return

    for i in range(level):
        if i == 0:
            nxt = now[1:]
            nxt_total = total + now[1]
        elif i == level - 1:
            nxt = now[:-1]
            nxt_total = total + now[-2]
        else:
            nxt = now[:i] + now[i + 1:]
            nxt_total = total + now[i - 1] * now[i + 1]

        if nxt in used and used[nxt] >= nxt_total:
            continue

        used[nxt] = nxt_total
        dfs(level - 1, nxt, nxt_total)


for tc in range(1, TC + 1):
    N = int(input())
    lst = tuple(map(int, input().split()))

    result = 0
    used = dict()
    used[lst] = 0

    dfs(N, lst, 0)

    print(f'#{tc} {result}')
