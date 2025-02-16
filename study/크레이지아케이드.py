lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

# 7*7 배열
# A는 5칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# B는 3칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# '#'은 벽이다
# 벽 그리고 A,B 뒤로는 물풍선이 터지지 않는다.
# 물을 피할곳은 지도상 몇군데인가? - 16 -

def boom(y, x, power):
    for i in range(4):
        for p in range(1, power+1):
            ny = y+dy[i]*p
            nx = x+dx[i]*p
            if ny<0 or nx<0 or ny>=7 or nx>=7: break
            if lst[ny][nx] == 'A' or lst[ny][nx] == 'B' or lst[ny][nx] == '#': break
            lst[ny][nx] = '@'

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(7):
    for j in range(7):
        if lst[i][j] == 'B':
            boom(i, j, 3)
        elif lst[i][j] == 'A':
            boom(i, j, 5)

cnt = 0
for i in range(7):
    for j in range(7):
        if lst[i][j] == '_':
            cnt+=1

print(cnt)
print('\n'.join(' '.join(row) for row in lst))