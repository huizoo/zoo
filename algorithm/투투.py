def boom(level, score):
    global max_score
    if level == N:
        if max_score < score:
            max_score = score
        return
    length = len(balloons)
    for i in range(length):
        target = balloons.pop(i)
        if length == 1:
            boom(level+1, score+target)
        elif i == 0:
            boom(level+1, score+balloons[i])
        elif i == length - 1:
            boom(level+1, score+balloons[i-1])
        else:
            boom(level+1, score+balloons[i-1]*balloons[i])
        balloons.insert(i, target)

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0
    boom(0, 0)
    print(f'#{tc} {max_score}')