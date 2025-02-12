# arr = [3,4,5,1,6,9]

# cnt = 0
# Sum = arr[0]
# def abc(level):
#     global Sum
#     print(Sum, end=' ')
#     if level == 5:
#         return
#     Sum += arr[level+1]
#     abc(level+1)
#
# abc(0)


# Sum = arr[0]
#
# def abc(level):
#     global Sum
#     if level == 5 :
#         print(Sum, end=' ')
#         return
#     Sum += arr[level+1]
#     abc(level+1)
#     Sum -= arr[level+1]
#     print(Sum, end=' ')
#
# abc(0)


# def abc(level, Sum):
#     if level == 5:
#         print(Sum, end=' ')
#         return
#
#     abc(level+1, Sum+arr[level+1])
#     print(Sum, end=' ')
#
# abc(0, arr[0])


# arr = [2, 0, 1, 1, 3, 5, 1]
# def abc(level):
#     if level >= len(arr):
#         return
#     abc(level+arr[level])
#     print(arr[level])
#
# abc(0)

# arr = [3,7,1,2]
# Sum = 0
# def abc(level):
#     global Sum
#     if level == 3:
#         print(Sum, end=' ')
#         return
#     for i in range(4):
#         Sum += arr[i]
#         abc(level+1)
#         Sum -= arr[i]
# abc(0)
#

# arr = [3,4,7,1,6]
# n = int(input())
#
# cnt = 0
# def abc(level, Sum):
#     global cnt
#     if Sum > 10: # 백트래킹
#         return
#     if level == n:
#         if Sum == 10:
#             cnt += 1
#         return
#     for i in range(5):
#         abc(level+1, Sum+arr[i])
#
# abc(0, 0)
# print(cnt)


# arr = ['A','B','C']
# path = ['']*2
# def abc(level):
#     if level == 2:
#         print(*path)
#         return
#     for i in range(3):
#         path[level] = arr[i]
#         abc(level+1)
#
# abc(0)



# n = int(input())
# arr = [1, 2, 3, 4, 5, 6]
# path = ['']*n
# def dice(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(6):
#         path[level] = arr[i]
#         dice(level+1)
# dice(0)


#
# card="ABCD"
# path=[""]*3
#
# def abc(level,start):
#     if level==3:
#         print(*path)
#         return
#
#     for i in range(start,4):
#         path[level]=card[i]
#         abc(level+1,i+1)
#         path[level]=0   # 있어도 되고 없어도 됨
#
# abc(0,0)



# n = int(input())
# dice = ['A', 'B', 'C', 'D']
# path = ['']*n
#
# def dfs1(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         if dice[i] != 'B':
#             path[level] = dice[i]
#             dfs1(level+1)
#
# def dfs2(level):
#     if 'B' in path:
#         return
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = dice[i]
#         dfs2(level+1)

# dfs1(0)
# print()
# dfs2(0)

# n = int(input())
# dice = ['A', 'B', 'C', 'D']
# path = ['']*n

# def dfs3(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         if level > 0 and path[level-1] == dice[i]:continue
#         path[level] = dice[i]
#         dfs3(level+1)
#
# dfs3(0)



# n = int(input())
# dice = ['A', 'B', 'C', 'D']
# path = ['']*n
#
# def dfs4(level):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         if level == 0 and i == 2:continue
#         path[level] = dice[i]
#         dfs4(level+1)
#
# dfs4(0)


'''
DFS BFS
'''


# name = ['Amy', 'Bob', 'Charles', 'Diane', 'Edger']
# arr=[
#     [0,1,0,0,0],
#     [0,0,1,0,0],
#     [0,0,0,0,0],
#     [0,0,1,0,1],
#     [1,0,1,0,0]]
# like = 0
# arr = list(zip(*arr))
# for row in arr:
#     if like < row.count(1):
#         like = row.count(1)
#         popular = name[arr.index(row)]
# print(popular)
#

# arr = ['A','B','C','D','E','F']
# table = [
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
#
# ch = input()
# idx = ord(ch)-65
# parents=-1
# bro=-1
# for i in range(6):
#     if arr[i][idx]==1:
#         parents=i
#         break
# if parents==-1:
#     print('형제없음')
# else:
#     for i in range(6):
#         if arr[parents][i]==1 and i!=idx:
#             bro=i
#             break
#     if bro == -1:
#         print('형제없음')
#     else:
#         print(chr(ord('A') + bro))



# name = ['A','B','C','D','E','F']
# arr = [
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
# def dfs(n):
#     print(name[n],end=' ')
#     for i in range(6):
#         if arr[n][i] == 1:
#             dfs(i)
#
# dfs(0)


# n,m=map(int,input().split())
# arr=[[] for _ in range(6)]
# for i in range(m):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#
# lst=['A','B','C','D','E','F']   # << 리스트 없으면
# def dfs(now):
#     print(lst[now],end=' ')     # lst[now]를 chr(now+65)로 교체
#     for i in arr[now]:
#         dfs(i)
# dfs(0)



# name="BACD"
# arr=[
#     [0,0,1,7],
#     [1,0,4,0],
#     [1,0,0,1],
#     [0,0,0,0]]
# used=[0]*4
# Min=21e8
#
# def dfs(now,Sum):
#     global Min
#     if name[now]=='D':
#         if Sum<Min:
#             Min=Sum
#
#     for i in range(4):
#         if arr[now][i]>0 and used[i]==0:
#             used[i]=1
#             dfs(i,Sum+arr[now][i])
#             used[i]=0
#
#
# used[1]=1
# dfs(1,0) # 탐색을 시작하는 index /// Sum
# print(Min)