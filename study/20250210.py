'''
원하는 값 찾을 때 함수로 구현하기 연습해보기
'''
# def seq_search(a, n, key) :
#     i = 0
#     while i < n and a[i] != key :
#             i += 1
#     if i < n : return i
#     return -1
#
# arr = [4, 9, 11, 23, 2, 19, 7]
#
# print(seq_search(arr, len(arr), 11))
#

# arr2 = [2, 4, 7, 9, 11, 19, 23]
# def seq_search2(a, n, key):
#     i = 0
#     while i < n and a[i] < key:
#         i += 1
#     if i < n and a[i] == key:
#         return i
#     else:
#         return -1
#
# print(seq_search2(arr2, len(arr2), 24))
#
# def seq_search22(a, n, key):
#     for i in range(n) :
#         if a[i] == key:
#             return i
#         elif a[i] > key:
#             return -1
#     return -1
# print(seq_search22(arr2, len(arr2), 19))
#
#

# # 위아래좌우 좌표들의 합이 가장 큰 곳의 합과. 좌표값 출력하기
#
# arr=[[1,2,3,4],
#     [1,2,9,4],
#     [1,9,3,9],
#     [1,2,9,4]]
#
# dy = [-1, 0, 0, 1]
# dx = [0, -1, 1, 0]
#
# def sum_arr(y, x) :
#     ret = 0
#     for i in range(4) :
#         ny, nx = y+dy[i], x+dx[i]
#         if 0 <= ny < 4 and 0 <= nx < 4 :
#             ret += arr[ny][nx]
#     return ret
#
# max_sum = 0
# y, x = 0, 0
# for i in range(4) :
#     for j in range(4) :
#         temp_sum = sum_arr(i, j)
#         if max_sum < temp_sum :
#             max_sum = temp_sum
#             y, x = i, j
# print(f'{max_sum} ({y},{x})')


# 모든 좌표로 부터 상하좌우 값 확인한다.

# 규칙 1.
# 기준 좌표로 부터 상하좌우의 범위가 배열범위를 넘어가면 무조건 0점처리

# 규칙 2.
# 1. 상하좌우의 합에서 기준좌표의 값을 뺀다.
# 1-1 상하좌우의 합에서 기준좌표의 값을 뺀 값이 음수라면 0점
# 1-2 상하좌우의 합에서 기준좌표의 값을 뺀 값이 짝수면 점수 2배하기

# 입력예제
# 테스트케이스의 개수를 입력 받는다.
# 배열의 크기 N을 입력받은후 N * N 사이즈 배열에 들어갈 값을 입력 받는다.

# 출력결과
# 상하좌우의 합중 Max값 출력하기

# 3
# 3
# 1 1 1
# 1 5 1
# 1 1 1
# 3
# 1 1 1
# 1 1 1
# 1 1 1
# 4
# 1 1 1 1
# 1 3 1 1
# 1 4 2 1
# 1 1 1 1
#
# #1 0
# #2 3
# #3 12  -- 짝수일때 (구한값 6에 곱하기 2하면 12가 됨)

# def find_score(y, x) :
#     dy = [-1, 0, 0, 1]
#     dx = [0, -1, 1, 0]
#     score = 0
#     for i in range(4) :
#         ny, nx = y+dy[i], x+dx[i]
#         if ny < 0 or ny >= N or nx < 0 or nx >= N :
#             return 0
#         else :
#             score += arr[ny][nx]
#     score -= arr[y][x]
#     if score < 0 :
#         return 0
#     elif score % 2 == 0 :
#         return score*2
#     else :
#         return score
#
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_score = int(-21e8)
#     for i in range(N) :
#         for j in range(N) :
#             score = find_score(i, j)
#             if max_score < score :
#                 max_score = score
#     print(f'#{tc} {max_score}')

'''
Binary Search
'''
#
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
# def binary_search(start, end, key) :
#     while start <= end :
#         mid = (start + end) // 2
#         if arr[mid] == key :
#             return mid
#         elif arr[mid] < key :
#             start = mid + 1
#         elif arr[mid] > key :
#             end = mid - 1
#     return -1
#
# print(binary_search(0, n-1, target))


'''
parametric search
'''

# bettery1 = "###_______"
# bettery2 = "__________"
# bettery3 = "##########"
#
# def parametric_search(st):
#     Max = -1
#     start = 0
#     end = len(st) - 1
#     while start <= end :
#         mid = (start + end) // 2
#         if st[mid] == '#':
#             Max = mid
#             start = mid + 1
#         elif st[mid] == '_':
#             end = mid - 1
#     return Max+1
# max1 = (parametric_search(bettery1)) * 10
# max2 = (parametric_search(bettery2)) * 10
# max3 = (parametric_search(bettery3)) * 10
# print(f'{max1}%')
# print(f'{max2}%')
# print(f'{max3}%')


# 워드작업 중 정전으로 인하여 컴퓨터가 강제로 종료가 되었습니다.
# 다시 전기가 들어어 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을때 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그래밍을 완성해 주세요.
# 시간복잡도 (On^2)보다 빨라야 합니다.

# 6*10 size 리스트 (배열)

# curser=[
#     '##########',
#     '##########',
#     '###_______',
#     '__________',
#     '__________',
#     '__________']
#
# def ps(arr) :
#     y, x = 0, 0
#     flag = 0
#     while 0 <= y < 6 :
#         start = 0
#         end = len(arr[0]) - 1
#         while start <= end :
#             mid = (start + end) // 2
#             if arr[y][mid] == '#' :
#                 x = mid
#                 start = mid + 1
#             elif arr[y][mid] == '_' :
#                 end = mid - 1
#                 flag = 1
#         if flag :
#             return y, x+1
#         y += 1
#     return y, x+1
# y, x = ps(curser)
# print(y, x)


def bbq(level) :
    if level == n :
        return
    print(level, end=' ')
    bbq(level + 1)
    print(level, end=' ')

n = int(input())
bbq(0)
