def bong1(level, y, x, Sum):
    global Max
    if level == 3:
        if Max < Sum:
            Max = Sum
        return
    if x % 2 == 1:
        for i in range(6):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if used[ny][nx] == 1: continue
            used[ny][nx] = 1
            bong1(level + 1, ny, nx, Sum + arr[ny][nx])
            used[ny][nx] = 0
    elif x % 2 == 0:
        for i in range(6):
            ny, nx = y - dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if used[ny][nx] == 1: continue
            used[ny][nx] = 1
            bong1(level + 1, ny, nx, Sum + arr[ny][nx])
            used[ny][nx] = 0

def bong2(y, x, Sum):
    global Max
    if x % 2 == 1:
        Sum2 = 0
        for i in range(1, 6, 2):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            Sum2 += arr[ny][nx]
        if Max < Sum+Sum2:
            Max = Sum+Sum2
        Sum2 = 0
        for i in range(0, 6, 2):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            Sum2 += arr[ny][nx]
        if Max < Sum + Sum2:
            Max = Sum + Sum2
    elif x % 2 == 0:
        Sum2 = 0
        for i in range(1, 6, 2):
            ny, nx = y - dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            Sum2 += arr[ny][nx]
        if Max < Sum + Sum2:
            Max = Sum + Sum2
        Sum2 = 0
        for i in range(0, 6, 2):
            ny, nx = y - dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            Sum2 += arr[ny][nx]
        if Max < Sum + Sum2:
            Max = Sum + Sum2

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    used = [[0]*M for _ in range(N)]
    dy = [0, -1, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 0, 1]
    for y in range(N):
        for x in range(M):
            used[y][x] = 1
            bong1(0, y, x, arr[y][x])
            # used[y][x] = 0
            bong2(y, x, arr[y][x])

    print(f'#{tc} {Max}')