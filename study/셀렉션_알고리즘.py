def quickselect(arr, k):
    k = k - 1  # 1-based index -> 0-based index로 변환
    pivot = arr[len(arr) // 2]  # 중간값을 피벗으로 선택
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    if k < len(smaller):  # k번째 값이 작은 그룹에 있을 경우
        return quickselect(smaller, k)
    elif k < len(smaller) + len(equal):  # k번째 값이 피벗일 경우
        return pivot
    else:  # k번째 값이 큰 그룹에 있을 경우
        return quickselect(larger, k - len(smaller) - len(equal))


# 예제 사용
arr = [7, 2, 1, 6, 8, 5, 3, 4]
k = 3
print(quickselect(arr, k))  # 출력: 3
