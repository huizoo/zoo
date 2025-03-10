# 예시 - argument랑 parameter 개수가 다를경우
# 1. default parameter



# 함수가 종료되면... 호출한 곳으로 돌아간다
# def getSum(a, b, c=3) : # 매개변수 parameter
#     return a+b+c

# result = getSum(3, 7) # 인자값 argument
# print(result)

# 2. packing unpacking

# num= [1,2,3,4,5]
# num2=(1,2,3,4,5)
# print(num,num2)

# a,b,*c=num2
# print(a,b,c)
# print(c)
# def getsum(*a) : 
#     print(type(a))
#     return a[0]+a[1]+a[2]

# result = getsum(1,2,3)
# print(result)


# def print_info(**args) : 
#     print(args)
#     print(type(args))
#     for i,j in args.items() : 
#         print(i,j)

# print_info(kevin=1, john=2, bob=3)

# aa=3
# bb=5

# def test() : 
#     global aa, bb
#     print(aa,bb)
#     aa+=1
#     bb+=1
#     print(aa,bb)

# test()
# print(aa,bb)

# def kfc() : 
#     print(aa, bb)
#     aa+=1
#     bb+=1
#     print(aa, bb)
# def test() : 
#     global aa, bb
#     aa=3
#     bb=5
#     print(aa,bb)

# test()
# kfc()

# 파이썬 내장함수 중 - map zip filter lambda 함수
# map - 리스트나 튜플같이 순회가 가능한 데이터구조의 값에
    # 일괄적으로 함수를 적용할 때 사용
    # 반환값은 map객체를 반환!!!
    # map(함수, iterables)

# num =['1','2','3']

# lst1=[]
# for i in num : 
#     lst1.append(int(i))
# print(lst1)

# lst2=map(int, num)
# print(lst2)
# print(list(lst2))

# a, b, c = map(int, input().split())

# lst3 = list(map(int, input().split()))

# zip 순회가능한 객체를 인자로 받고 각 요소를 잘라서
# 튜플을 원소로 하는 객체를 반환한다.

# a = '12345'
# b = 'qwert'
# ret=zip(a,b)
# print(ret)
# print(list(ret))

# a = '12345'
# b = 'qwert'
# c = 'asdfg'
# for i in zip(a,b,c) : 
#     print(list(i))

# for x,y,z in zip(a,b,c) : 
    # print(x,y,z)

# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]

# for x, y, z in zip(*arr) : 
#     print(x, y, z)

# for i in range(3) : 
#     for j in range(3) : 
#         print(f'{i} {j}')

# arr = [[1,2,3],[4,5,6],[7,8,9]]

# for i in zip(arr[0], arr[1], arr[2]) : # 1번 방법
#     print(list(i))

# for i in zip(*arr) : # 2번 방법
#     print(list(i))

# arr = list(map(list,zip(*arr))) # 3번 방법

# for i in range(3) : # 3-1번 방법
#     for j in range(3) : 
#         print(arr[i][j], end=' ')
#     print()

# print('\n'.join(' '.join(map(str, row)) for row in arr)) # 3-2번 방법


# filter
# 리스트나 튜플과 같이 순회 가능한 데이터 구조의 값들에 함수를 적용
# 적용후 값이 True 인 것들만 반환 (filter 라는 객체(이터레이터...?)로 반환)

# num = list(range(1,10))

# def get_even(value) : 
#     if value%2 == 0 : 
#         return True
#     else :
#         return False
#     return True if value%2==0 else False

# ret = filter(get_even, num)
# print(ret)
# print(list(ret))


# lambda (이름이 없는 익명함수)

# def Sum(a,b) : 
#     return a+b
# result=Sum(3,5)


# result=(lambda a,b : a+b)(3,5)
# print(result)

# result=(lambda a,b : a+b)
# print(result(3,5))

# lst1 = [1,2,3,4,5]                            # 문제
# lst2 = [6,7,8,9,10]

# result = list(zip(lst1, lst2))                # 1번 답
# for i in range(5) : 
#     print(sum(result[i]), end=' ')
# print()

# for i in range(5) :                           # 2번 답
#     print(lst1[i]+lst2[i], end=' ')
# print()

# result = lambda x,y : x+y                     # 3번 답
# lst3=map(result,lst1,lst2)
# print(*lst3)

# lst4 = map(lambda x,y : x+y, lst1, lst2)      # 4번 답
# print(*lst4)

# arr = []
# for i in range(100) : 
#     if i % 2 == 0 : 
#         arr.append(i)

# print(arr)

# result=filter(lambda even:even%2==0, range(100))
# print(list(result))



# 재귀함수 recursion
# 주사위 1개 던졌을 때 나오는 모든 경우의 수

# for i in range(1,7) : 
#     print(i)

# # 주사위 2개 던졌을 때..
# for i in range(1,7) : 
#     for j in range(1,7) : 
#         print(i,j)



# 주사위 n개 던졌을 때..

n = int(input())

path=[0]*n

def abc(level):
    if level==n:
        for i in range(n) : 
            print(path[i], end=' ')
        print()
        return
    for i in range(6) : 
        path[level] = i+1
        abc(level+1)


abc(0)