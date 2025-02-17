T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))

    def check(score, i):
        if len(score) == 1 and i == 0:
            return score[i]
        elif i == 0:
            return score[i + 1]
        elif i == len(score) - 1:
            return score[i - 1]
        elif 0 < i < len(score) - 1:
            return score[i + 1] * score[i - 1]
        else:
            return 0

    Max = -21e8

    def dfs(level, Sum=0):
        global Max, score, cnt
        if len(score) == 0:
            Max = max(Max, Sum)
            return

        for i in range(len(score)):
            if level < N - 2 and (i == 0 or i == len(score) - 1):
                continue
            cha = score[i]
            ret = check(score, i)
            score.pop(i)
            dfs(level + 1, Sum + ret)
            score.insert(i, cha)


    dfs(0)
    print(f'#{tc} {Max}')