# arr = [1, 2, 3, 4, 2, 5, 3, 1, 1, 2, 5]
# N = len(arr)
# L, R = 0, 1  # 투 포인터 초기화
# cnt = 0
# Sum = arr[0]
#
# while L < N:
#     if Sum == 5:  # 부분합이 5인 경우 카운트 증가
#         cnt += 1
#         Sum -= arr[L]  # 왼쪽 포인터 이동
#         L += 1
#     elif Sum > 5:  # 부분합이 5보다 크면 왼쪽 포인터 이동
#         Sum -= arr[L]
#         L += 1
#     else:  # 부분합이 5보다 작으면 오른쪽 포인터 이동
#         if R < N:
#             Sum += arr[R]
#             R += 1
#         else:  # R이 범위를 초과하면 종료
#             break
#
# print(cnt)


# # lambda 적용하기
# lst1 = [1,2,3,4,5]
# lst2 = [6,7,8,9,10]
# lst3 = list(map(lambda x, y: x + y, lst1, lst2))
# print(lst3)



# arr=[0]*200
# def findboss(member):
#     global arr
#     if arr[ord(member)]==0: # 비어있으면 자기 자신이 보스
#         return member
#     ret=findboss(arr[ord(member)])
#     return ret
#
# def union(a,b):
#     global arr
#     bossA,bossB=findboss(a),findboss(b)
#     if bossA==bossB: # 둘의 보스가 같으면 함수 종료
#         return
#     arr[ord(bossB)]=bossA # 둘의 보스가 다르면 하나에 보스 등록
#
# union('A','B')
# union('D','E')
# union('B','E')
# union('B','D')
# union('E','F')
#
# y,x=input().split()
# if findboss(y)==findboss(x):
#     print('같은그룹')
# else: print('다른그룹')




# 5 5
# A B
# B C
# D E
# A D
# C D
#
# 6 4
# A B
# B D
# F D
# A E



# arr=[0]*200
# n,m=map(int,input().split())
# edge=[]
# for _ in range(m):
#     edge.append(input().split())
# def findboss(m):
#     global arr
#     if arr[ord(m)]==0: return m
#     ret=findboss(arr[ord(m)])
#     arr[ord(m)]=ret
#     return ret
#
# def union(a,b):
#     global arr
#     fa,fb=findboss(a),findboss(b)
#     if fa==fb:
#         return 1
#     arr[ord(fb)]=fa
#
# answer=0
# for i in range(m):
#     a,b=edge[i]
#     ret=union(a,b)
#     if ret:
#         answer=1
#         break
# if answer:
#     print("cycle 발생")
# else: print("cycle 없음")






# 5
# 8
# A B 9
# A C 3
# A E 7
# B C 14
# B D 11
# C D 1
# C E 5
# A D 20



# k=int(input()) # 정점의 개수
# n=int(input()) # 간선 정보의 개수
# lst=[list(input().split()) for _ in range(n)]
# lst.sort(key=lambda x:int(x[2]))
# arr=[0]*200
#
# def findboss(m):
#     if not arr[ord(m)]:
#         return m
#     ret=findboss(arr[ord(m)])
#     arr[ord(m)]=ret
#     return ret
#
# def union(a,b,i):
#     global arr,cnt,total_cost
#     a_boss,b_boss=findboss(a),findboss(b)
#     if a_boss==b_boss:
#         return
#     total_cost+=int(lst[i][2])
#     cnt+=1
#     arr[ord(b_boss)]=a_boss
#
# total_cost=0 # 최종 비용
# cnt=0 # 연결되는 간선의 개수
# for i in range(n):
#     if cnt==k-1:
#         print(total_cost)
#         break
#     union(lst[i][0],lst[i][1],i)






def find(parent, x):  # 부모 노드를 찾는 함수 (경로 압축)
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, a, b):  # 두 집합을 합치는 함수 (유니온)
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:  # 랭크가 높은 쪽이 부모가 됨
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
            if rank[rootA] == rank[rootB]:
                rank[rootB] += 1


def kruskal(n, edges):
    parent = {chr(i): chr(i) for i in range(ord('A'), ord('A') + n)}  # 부모 테이블
    rank = {chr(i): 0 for i in range(ord('A'), ord('A') + n)}  # 랭크 정보
    edges.sort(key=lambda x: x[2])  # 가중치 기준 정렬

    mst_cost = 0
    mst_edges = []

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):  # 사이클이 없으면 선택
            union(parent, rank, u, v)
            mst_edges.append((u, v, weight))
            mst_cost += weight

    return mst_cost, mst_edges


n = int(input())  # 노드 개수
m = int(input())  # 간선 개수
edges = []
for _ in range(m):
    u, v, w = input().split()
    edges.append((u, v, int(w)))

mst_cost, mst_edges = kruskal(n, edges)


print(mst_cost)