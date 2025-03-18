# 한 달 후면 국가의 부름을 받게 되는 정싸피는 여행을 가려고 한다.
# 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에,
# 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
# 정싸피가 여행에 필요하다고 생각하는 N개의 물건이 있다.
#
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 정싸피가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 정싸피는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 정싸피가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
#
# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 정싸피가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와
# 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
# 입력으로 주어지는 모든 수는 정수이며 제한시간은 2초 이다.
#
# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
#
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
#
# 출력
# 14

# N, K = map(int, input().split())
# # 0번 인덱스는 물건의 무게, 1번 인덱스는 물건의 가치
# arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
#
# result = [[0]*(K+1) for _ in range(N+1)]
#
# for i in range(1, N+1):
#     weight, worth = arr[i]
#     for j in range(1, K+1):
#         if weight > j:
#             result[i][j] = result[i-1][j]
#         else:
#             result[i][j] = max(result[i-1][j], worth + result[i-1][j-weight])
# print(result[N][K])








# 7 1 10 원짜리 동전이 있다
# 14원 거슬러 줄때 최소동전의 개수?
#
# n - 동전의 종류 개수
# k - 거슬러줄 돈
# 사용할 동전입력받기
#
# 입력예제
# 3 14
# 7
# 1
# 10

# 출력결과
# 2

# N, K = map(int, input().split())
#
# arr = [0]
# for _ in range(N):
#     arr.append(int(input()))
#
# arr.sort()
#
# result = [0] + [21e8]*K
#
# for i in range(1, N+1):
#     coin = arr[i]
#     for j in range(coin, K+1):
#         if result[j-coin] != 21e8:
#             result[j] = min(result[j], 1+result[j-coin])
#
# if result[K] == 21e8:
#     print(-1)
# else:
#     print(result[K])




# LCS : 최장 공통 부분 문자열 Longest common substring
# BABJYP
# ABCBJY
# -> BJY

# st = input()
# st2 = input()
# n = len(st)
# n2 = len(st2)
# arr = [[0]*(n+1) for _ in range(n2+1)]
# Max = 0
# for i in range(1, n+1):
#     for j in range(1, n2+1):
#         if st[i-1] == st2[j-1]:
#             arr[i][j] = arr[i-1][j-1] + 1
#             Max = max(Max, arr[i][j])
#         else:
#             arr[i][j] = 0
#
# print(Max)






# LCS : 최장 공통 부분 수열 Longest common subsquence
# BABJYP
# ABPABY
#  -> B A B Y

# st = input()
# st2 = input()
# n = len(st)
# n2 = len(st2)
# arr = [[0]*(n+1) for _ in range(n2+1)]
# Max = 0
# for i in range(1, n+1):
#     for j in range(1, n2+1):
#         if st[i-1] == st2[j-1]:
#             arr[i][j] = arr[i-1][j-1] + 1
#         else:
#             arr[i][j] = max(arr[i][j-1], arr[i-1][j])
#
#         Max = max(Max, arr[i][j])
#
# print(Max)
#




# LIS : 최장 증가 부분 수열 Longest increasing subsquence
# 10 20 10 30 20 50
#  -> 10 20 30 50



# arr = list(map(int, input().split()))
# N = len(arr)
# result = [1]*N
#
# for i in range(N):
#     now = arr[i]
#     for j in range(i+1):
#         if arr[j] < now:
#             result[i] = max(result[j] + 1, result[i])
#
# print(max(result))