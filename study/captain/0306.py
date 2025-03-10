import copy

# from collections import deque
# # 사이클이 있을 땐 사용 못한다
# name = ['CS', 'language', 'pjt', 'algo', 'data_structure', 'cote', 'developer']
# arr = [
#     [0,0,1,0,0,0,0],
#     [0,0,0,1,1,0,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
# ]
#
# acc = [0]*7
# used = [0]*7
#
# # # 사전 작업 개수 파악
# # for j in range(7):
# #     for i in range(7):
# #         if arr[i][j] == 1:
# #             acc[j] += 1
# #
# # # 사전작업 없이 바로 시작할 수 있는 작업은
# # # 큐에 넣고 used 에 1체크 해주기
# # q = deque()
# # for i in range(7):
# #     if acc[i] == 0:
# #         used[i] = 1
# #         q.append(i)
# #
# # # bfs 돌리면서 작업순서 큐에 넣기
# # while q:
# #     now = q.popleft()
# #     print(name[now], end=' ')
# #     for i in range(7):
# #         if arr[now][i] == 1 and used[i] == 0:
# #             if acc[i] == 1:
# #                 acc[i] = 0
# #                 used[i] = 1
# #                 q.append(i)
# #             else:
# #                 acc[i] -= 1


# power=[50,40,99,5,25,6,37]
# team1 = []
# team2 = power[:]
# Min = 10e8
# def dfs():
#     global Min
#     Min = min(Min, abs(sum(team1)-sum(team2)))
#     for i in range(len(team2)):
#         team1.append(team2.pop(i))
#         dfs()
#         team2.insert(i, team1.pop())
# dfs()
# print(Min)




arr=[
    [3,1,9,6],
    [6,5,9,6],
    [5,8,3,7],
]
d = [(-1, 0), (0, -1), (0, 1), (1, 0), (0, 0)]
Max = 0
def dfs(x, lst):
    global Max
    if x == 4:
        Sum = 0
        for i in range(3):
            for j in range(4):
                Sum += lst[i][j]
        Max = max(Sum, Max)
        return
    for i in range(3):
        for j in range(4):
            temp = copy.deepcopy(lst)
            for dy, dx in d:
                ny, nx = i+dy, j+dx
                if ny<0 or nx<0 or ny>=3 or nx>=4:continue
                temp[ny][nx] = (temp[ny][nx]*7) % 10
            dfs(x+1, temp)

dfs(0, arr)
print(Max)