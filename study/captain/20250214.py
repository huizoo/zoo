# a, b = 4, 5
# arr = [
#     [(1, 3), (2, 8)],
#     [(2, 1), (3, 8)],
#     [(3, 1)],
#     [],
# ]
#
# def dfs(now, Sum):
#     global Min
#     if now == 3:
#         if Min > Sum:
#             Min = Sum
#     for i in lst[now]:
#         if used[i[0]]: continue
#         used[i[0]]=1
#         dfs(i[0], Sum+i[1])
#         used[i[0]]=0
#
#
# n, m = map(int, input().split())
# lst = [[] for _ in range(n)]    # 정점의 개수만큼 리스트 추가
# for i in range(m):
#     s,e,c = map(int, input().split())
#     lst[s].append((e, c))
#     lst[e].append((s, c))   # 무방향(양방향) 그래프면 추가
# Min = 21e8
# used = [0]*4
# dfs(0, 0)
# print(Min)



# arr = [
#     [4, 5, 2],
#     [-2, 1, 6],
#     [3, 9, -4],
#     [3, 5, 2],
# ]
# path = []
# def dfs(n, Sum):
#     global cnt
#     if n == 4:
#         if Sum >= 20:
#             print(*path)
#             cnt += 1
#         return
#     for i in range(3):
#         path.append(arr[n][i])
#         dfs(n+1, Sum + arr[n][i])
#         path.pop()
# cnt = 0
# dfs(0, 0)
# print(cnt)

#
# arr = [
#     [3,5,9,6],
#     [7,-8,1,6],
#     [-10,2,3,9],
#     [5,1,2,8],
#     [4,7,1,8],
# ]
# cnt = 0
# def dfs(n, k, Sum):
#     global cnt
#     if n == 4:
#         if Sum >= 30:
#             print(*path)
#             cnt += 1
#         return
#     for i in range(-1, 2):
#         if 0 <= k + i < 4:
#             path.append(arr[n+1][k+i])
#             dfs(n+1, k+i, Sum+arr[n+1][k + i])
#             path.pop()
#
# for j in range(4):
#     path = [arr[0][j]]
#     dfs(0, j, arr[0][j])
# print(cnt)


# arr = [
#     [0,0,0,0],
#     [1,0,1,0],
#     [1,0,1,0],
#     [0,0,0,0],
# ]
# dy = [0,0,-1,1]
# dx = [-1,1,0,0]
# flag = 0
# visited = [[0]*4 for _ in range(4)]
# def dfs(y, x):
#     global flag
#     if y == 3 and x == 3:
#         flag = 1
#         return
#
#     for i in range(4):
#         ny = y+dy[i]
#         nx = x+dx[i]
#         if ny<0 or nx<0 or ny>3 or nx>3: continue
#         if arr[ny][nx] == 1:continue
#         if visited[ny][nx]==1:continue
#         visited[ny][nx]=1
#         dfs(ny,nx)
#         if flag:
#             return
#
# visited[0][0] = 1
# dfs(0,0)
# if flag:
#     print('도착가능')
# else:
#     print('방탈출못함')




# arr = [
#     [0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0],
# ]
# end = [2, 3]
# Min = 21e8
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0, 0]
# visited = [[0]*6 for _ in range(5)]
# def dfs(y, x, cnt):
#     global Min, flag
#     if cnt > Min:
#         return
#     if y == 2 and x == 3:
#         if Min > cnt:
#             Min = cnt
#         return
#
#     for i in range(4):
#         ny, nx = y+dy[i], x+dx[i]
#         if ny<0 or nx<0 or ny>4 or nx>5:continue
#         if arr[ny][nx]: continue
#         if visited[ny][nx]: continue
#         visited[ny][nx] = 1
#         dfs(ny, nx, cnt+1)
#         visited[ny][nx] = 0
#
# dfs(0, 0, 0)
# print(Min)




arr = [
    [4,8,1],
    [9,2,6],
    [3,5,7],
]
Max = 0
dy = [0, 0, -1, 1, 0]
dx = [-1, 1, 0, 0, 0]
def dfs(level):
    global Max
    if level == 3:
        Sum = 0
        for k in range(3):
           Sum += sum(arr[k])
        if Sum > Max:
            Max = Sum
        return
    for y in range(3):
        for x in range(3):
            temp = [0, 0, 0, 0, 0]
            for i in range(5):
                ny, nx = y + dy[i], x + dx[i]
                if ny<0 or nx<0 or ny>2 or nx>2:continue
                temp[i] = arr[ny][nx]
                arr[ny][nx] = (arr[ny][nx] * 7) % 10
            dfs(level+1)
            for i in range(5):
                ny, nx = y + dy[i], x + dx[i]
                if ny<0 or nx<0 or ny>2 or nx>2: continue
                arr[ny][nx] = temp[i]

dfs(0)
print(Max)

