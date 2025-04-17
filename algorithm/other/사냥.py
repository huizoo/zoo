import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    monsters = []
    hunters = [(0, 0, 0)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                monsters.append((arr[i][j], i, j))
            elif arr[i][j] < 0:
                hunters.append((arr[i][j], i, j))
    monsters.sort(key=lambda x:x[0])
    hunters.sort(reverse=True, key=lambda x:x[0])
    Min = 1e9
    def cal_dist(y1, x1, y2, x2):
        return abs(y1-y2)+abs(x1-x2)

    def dfs(y, x, dist, target):
        global Min
        if Min < dist:
            return
        if not target:
            Min = dist

        for idx, (num, ty, tx) in enumerate(target):
            nxt_target = target[:]
            nxt_target.pop(idx)
            if num > 0:
                nxt_target.append(hunters[num])
                # nxt_target.insert(idx, hunters[num])
            dfs(ty, tx, dist+cal_dist(y, x, ty, tx), nxt_target)



    dfs(0, 0, 0, monsters)

    print(f'#{tc} {Min}')