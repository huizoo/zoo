# 선택, 삽입, 버블 정렬 -> n^2 속도

# 힙, 합병, 퀵 정렬 -> n*logn 속도

# 계수 정렬 -> n 속도

# mincoding 29.5 - 4 -> merge sort

# arr = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
#
# result = []
# idx = idx2 = 0
# while idx < 4 and idx2 < 4:
#     if arr[idx] < arr2[idx2]:
#         result.append(arr[idx])
#         idx += 1
#     else:
#         result.append(arr2[idx2])
#         idx2 += 1
#
# result += arr[idx:] + arr2[idx2:]
#
# print(*result)



# mincoding 23.5 - 5 -> quick sort

arr = list(map(int, input().split()))
pivot = arr[0]
start = 1
end = len(arr) - 1
while 1:
    while start < len(arr) and arr[start] <= pivot:
        start += 1
    while end > 0 and arr[end] >= pivot:
        end -= 1
    if start > end:
        arr[0], arr[end] = arr[end], arr[0]
        break
    arr[start], arr[end] = arr[end], arr[start]

print(*arr)
