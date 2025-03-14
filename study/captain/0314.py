# # 10
# # 18 21
# # 11 14
# # 15 17
# # 18 22
# # 13 16
# # 10 16
# # 12 23
# # 22 24
# # 16 20
# # 15 19
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(10)]
# arr.sort(key=lambda x:x[1])
# ed = 0
# cnt = 0
# for start, end in arr:
#     if start >= ed:
#         ed = end
#         cnt += 1
#
# print(cnt)






# # bottom-up
#
#
#
# arr = [0, 7, -3, -5, -4, -2, 6, 5, -9, 1, 0]
# dp = [0]*11
# for i in range(11):
#     if i % 2 == 0:
#         dp[i] = max(dp[i-1] + arr[i], dp[i-2] + arr[i], dp[i//2] + arr[i])
#     else:
#         dp[i] = max(dp[i-1] + arr[i], dp[i-2] + arr[i])
#
# print(dp[10])


# arr=[[0,5,3,6,8],
#      [1,4,2,9,1],
#      [6,9,1,7,7],
#      [8,5,4,1,0]]
#
# dp = [[0]*5 for _ in range(4)]
# # dp 배열을 만들어서 해도 되고
# for i in range(4):
#     for j in range(5):
#         if i == 0:
#             dp[i][j] = arr[i][j] + dp[i][j - 1]
#         elif j == 0:
#             dp[i][j] = arr[i][j] + dp[i - 1][j]
#         else:
#             dp[i][j] = arr[i][j] + min(dp[i][j - 1], dp[i - 1][j])
#
# print(dp[3][4])
#
# # arr 에 더해도 됨(재활용을 하지 않을 때)
# for i in range(4):
#     for j in range(5):
#         if i == 0:
#             arr[i][j] += arr[i][j] + dp[i][j - 1]
#         elif j == 0:
#             arr[i][j] += arr[i][j] + dp[i - 1][j]
#         else:
#             arr[i][j] += min(dp[i][j - 1], dp[i - 1][j])
#
# print(arr[3][4])


arr = [1, 0, 1, 1]
arr2 = [0, 0, 1, 0]
print(int(''.join(map(str, arr)), 2))
print(int(''.join(map(str, arr2)), 2))


Sum=0
for i in range(4):
    if arr[i]&1:
        Sum += 1<<(len(arr)-(i+1))
print(Sum)


