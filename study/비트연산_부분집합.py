# # 집합의 원소들 (예: ['a', 'b', 'c'])
# elements = ['a', 'b', 'c']
# n = len(elements)
#
# # 0부터 2^n - 1 까지 모든 비트마스크를 순회
# for mask in range(1 << n):
#     subset = []
#     for i in range(n):
#         # mask의 i번째 비트가 켜져 있다면, 해당 원소를 부분집합에 추가
#         if mask & (1 << i):
#             subset.append(elements[i])
#     print("부분집합:", subset)

arr = [-7,-5,2,3,8,-2,4,6,9]
cnt = 0
for mask in range(1<<9):
    subset = []
    for i in range(9):
        if mask & (1<<i):
            subset.append(arr[i])
    if sum(subset) == 0:
        cnt +=1
        print(f'#{cnt} {subset}')