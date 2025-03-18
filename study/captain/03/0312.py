import heapq
#
# '''
# 최소힙
# '''
#
# # arr = []
# # heapq.heappush(arr,4)   # 리스트에 heap 자료구조의 규칙에 의거해서 자료를 저장
# # heapq.heappush(arr,6)
# # heapq.heappush(arr,1)
# # heapq.heappush(arr,2)
# # heapq.heappush(arr,3)
# #
# # for i in range(len(arr)):
# #     print(heapq.heappop(arr), end=' ') # heap 규칙에 따라 출력 nlogn
# #
# # while arr:
# #     temp = heapq.heappop(arr)
# #     print(temp, end=' ')
# #
#
# # arr = [3422, 5, 3, 1, 5]
# # heap = []
# # for i in range(len(arr)):
# #     heapq.heappush(heap, arr[i])
# #
# # for i in range(len(arr)):
# #     print(heapq.heappop(heap), end=' ')
# #
# #
# # arr = [3422, 5, 3, 1, 5]
# # heapq.heapify(arr)
# # print(arr)
# # for i in range(len(arr)):
# #     print(heapq.heappop(arr), end=' ')
# #
#
#
# '''
# 최대힙
# '''
# #
# # arr = [3422, 5, 3, 1, 5]
# # heap = []
# # for i in range(len(arr)):
# #     heapq.heappush(heap, -arr[i])
# # for i in range(len(arr)):
# #     print(-heapq.heappop(heap), end=' ')
# #
# #
# #
# # arr = [3422, 5, 3, 1, 5]
# # heap = []
# # for i in range(len(arr)):
# #     heapq.heappush(heap, (-arr[i], arr[i]))
# # print(heap)
# #
# # for i in range(len(arr)):
# #     print(heapq.heappop(heap)[1], end=' ')
# #
# #
# #
# # arr = [3422, 5, 3, 1 , 5]
# # heap=list(map(lambda x: -x, arr))
# # heapq.heapify(heap)
# # for i in range(len(arr)):
# #     print(-heapq.heappop(heap), end=' ')
#
#
#
#
# # '''
# # 문제
# # '''
# #
# # # import heapq
# # n = int(input())
# # heap = []
# # for _ in range(n):
# #     heapq.heappush(heap, int(input()))
# # Sum = 0
# # for _ in range(n-1):
# #     temp = heapq.heappop(heap) + heapq.heappop(heap)
# #     Sum += temp
# #     heapq.heappush(heap, temp)
# # print(Sum)
#
#
#
# # arr = [[1, 5], [1, 9], [4, 2]]
# # 우선순위 조건 1. 첫번째 원소 내림차순
# # 우선순위 조건 2. 두번째 원소 오름차순
# class Node:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __lt__(self, other): # less than < (작다) : self -> 앞에 놓여야 할 값 / # other : 뒤에 있는 값
#         # True 를 반환하면 self 가 other 보다 앞으로, False 는 반대로
#         # self 는 자기자신 객체, other 는 다른 객체 전부
#         if self.a > other.a: return True
#         if self.a < other.a: return False
#         return self.b < other.b
#
# heap = []
# heapq.heappush(heap, Node(1, 5))
# heapq.heappush(heap, Node(1, 9))
# heapq.heappush(heap, Node(4, 2))
# #
# while heap:
#     temp = heapq.heappop(heap)
#     print(temp.a, temp.b)


# heap = [(1, 5), (1, 9), (4, 2)]
# heap = list(map(lambda x: Node(x[0], x[1]), heap))
# heapq.heapify(heap)
# while heap:
#     temp = heapq.heappop(heap)
#     print(temp.a, temp.b)   # 정수형으로 출력




'''
다익스트라 알고리즘 조건
1. 가중치가 양수여야 함.
2. 시작점이 정해져있어야 함.
'''

name='ABCDE'
inf=int(21e8)
arr=[
    [0,3,inf,9,5],
    [inf,0,7,inf,1],
    [inf,inf,0,1,inf],
    [inf,inf,inf,0,inf],
    [inf,inf,1,inf,0]]
used=[0]*5
used[0]=1 # A(0번인덱스)를 시작점으로 등록
result=[0,3,inf,9,5] # 첫번째 경유지를 시작점인 A로 놓았을 경우

def select_ky():
    Min=int(21e8)
    Minindex=0
    for i in range(5):
        if used[i]==0 and result[i]<Min:
            Min=result[i]
            Minindex=i
    return Minindex

def dijkstra():
    # 경유지 선택
    for i in range(4):
        via=select_ky()
        used[via]=1

    # 시작->경유
    # 시작->경유->도착 비교 후 작은 값으로 갱신
        for j in range(5): # result 배열에 갱신 할 것임
            # 현재 기준 j로 갈 수 있는 최소값
            baro=result[j]
            # via 를 경유해서 j 로 가는 최소값
            # via 로 가는 최소값 + via 에서 j로 가는 값
            kyoung=result[via]+arr[via][j]
            if baro>kyoung:
                result[j]=kyoung
dijkstra()
print(*result)