import copy

def boom(level, score):
    global max_score
    arr = copy.deepcopy(balloons)
    if level == N:
        if max_score < score:
            max_score = score
        return
    for i in range(len(balloons)):
        target = balloons.pop(i)
        if len(balloons) == 1:
            boom(level+1, score+target)
        elif i == 0:
            boom(level+1, score+balloons[i+1])
        elif i == len(balloons)-1:
            boom(level+1, score+balloons[i-1])



t = int(input())
for tc in range(1, t+1):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0

    boom(0, 0)

    print(f'#{tc}')