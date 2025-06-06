from collections import deque
import sys

input = sys.stdin.readline

M, N, H = list(map(int, input().split()))

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

target = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k, 0))
            elif arr[i][j][k] == 0:
                target += 1

if target == 0:
    print(0)
    exit()

d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

day = 0

while q:
    z, y, x, now = q.popleft()
    day = now
    for dz, dy, dx in d:
        nz, ny, nx = z + dz, y + dy, x + dx
        if nz<0 or ny<0 or nx<0 or nz>=H or ny>=N or nx>=M: continue
        if arr[nz][ny][nx] != 0: continue
        arr[nz][ny][nx] = 1
        q.append((nz, ny, nx, now+1))
        target -= 1


if target == 0:
    print(day)
else:
    print(-1)