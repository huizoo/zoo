from collections import deque
import copy
#
# name = 'ABCDEF'
# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]]
#
# def bfs(start):
#     q = deque()
#     q.append(start)
#
#     while q:
#         now = q.popleft()
#         print(name[now], end=' ')
#         for i in range(6):
#             if arr[now][i]:
#                 q.append(i)
# bfs(0)
#

# name = 'BACD'
# arr = [
#     [0, 0, 0, 1],
#     [1, 0, 1 ,0],
#     [1, 0, 0, 1],
#     [0, 0, 0, 0],
# ]
# used = [0]*4
#
# def bfs(start):
#     q = deque()
#     q.append(start)
#     used[start] = 1
#     while q:
#         now = q.popleft()
#         print(name[now], end='')
#         for i in range(4):
#             if not used[i] and arr[now][i]:
#                 used[i] = 1
#                 q.append(i)
#
# bfs(1)

# name = 'ABCD'
# arr = [
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
#
# cnt = 0
# def bfs(start):
#     global cnt
#     q = deque()
#     used = [0]*4
#     used[start] = 1
#     q.append((start, used))
#
#     while q:
#         now, path = q.popleft()
#         if now == 3:
#             cnt += 1
#         for i in range(4):
#             if arr[now][i] == 1 and path[i] == 0:
#                 used=copy.deepcopy(path)
#                 used[i] = 1
#                 q.append((i,used))
#
# bfs(0)
# print(cnt)



#
# n=int(input())
# arr=[[0]*n for _ in range(n)]
# y,x=map(int,input().split())
#
# arr[y][x]=1
# q=deque()
# q.append((y,x))
#
# directy=[0,0,1,-1]
# directx=[1,-1,0,0]
# while q:
#     y,x=q.popleft()
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if dy<0 or dx<0 or dy>=n or dx>=n: continue
#         if arr[dy][dx]!=0: continue
#         arr[dy][dx]=arr[y][x]+1
#         q.append((dy,dx))
#
# for i in arr:
#     print(*i)
#

#
# n = int(input())
# arr = [[0]*n for _ in range(n)]
# y, x = map(int, input().split())
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# q = deque()
# q.append((y, x))
# arr[y][x] = 1
# while q:
#     y1, x1 = q.popleft()
#     for i in range(4):
#         ny, nx = y1+dy[i], x1+dx[i]
#         if ny<0 or nx<0 or ny>n-1 or nx>n-1:continue
#         if arr[ny][nx]:continue
#         arr[ny][nx] = arr[y1][x1] + 1
#         q.append((ny, nx))
#         if ny == 0 and nx == 1:
#             print(arr[ny][nx])
#
# print(arr[0][1])


# n = int(input()) # 5
# arr = [[0]*n for _ in range(n)]
# y1, x1 = map(int, input().split())
# y2, x2 = map(int, input().split())
#
# q = deque()
# q.extend([(y1, x1), (y2, x2)])
# arr[y1][x1] = 1
# arr[y2][x2] = 1
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# while q:
#     yy, xx = q.popleft()
#     for i in range(4):
#         ny, nx = yy+dy[i], xx+dx[i]
#         if ny<0 or nx<0 or ny>n-1 or nx>n-1:continue
#         if arr[ny][nx]:continue
#         arr[ny][nx] = arr[yy][xx] + 1
#         q.append((ny,nx))
# Max = 0
# for row in arr:
#     Max = max(Max, max(row))
#
# print(Max)
# for i in arr:
#     print(*i)