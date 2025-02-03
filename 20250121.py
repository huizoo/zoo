# a = 3.12523
# b = 2.72495


# print(f"{a:.2f}")
# print(f"{b:.2f}")

# print(round(a+1e-8, 2))
# print(round(b+1e-8, 2))

# print(round(a))
# print(round(b))

# print("오늘의 컨디션은 \"100%\" 입니다")

# s = 'abcdefg'

# print(s[:3])
# print(s[3:])
# print(s[2:5])
# print(s[5:2:-1])
# print(s[1:6:2])
# print(s[::-1])
# print(s[-2])

# lst=[1,2,3,4]
# lst[1]=22
# s='abcdefg'
# # s[1] = 'k' 문자열값 함부로 못바꿈
# ret=s.replace(s[1],'k')
# print(ret)


# list=[1,2,3,4]

# count = 0

# for _ in list : 
#     count += 1

# print(count)

# print(list*3)
# print(list+[7, 8, 9])


# lst = [1, 2, 3, 4, [5, 6, 7], 8]

# print(lst[4][0])
# print(lst[-2][-3])

# tp = (1, 2, 3, 4, 5)

# print(tp)
# print(type(tp))
# print(tp[1])
# print(len(tp))
# print(tp[-1])

# dic = {1:3, 2:{4:5}, '학':6, '교':[7,8,9]}

# print(dic)
# print(type(dic))
# print(dic[1])
# print(dic[2][4])
# print(dic['학'])
# print(dic['교'][2])

# dic[2] = '여름에는 민어탕이 아주 좋아'
# print(dic)
# dic[111] = dic.pop(1)
# print(dic)

# print(dic.pop('교'))

# print(dic)

# lst= [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,7,7]

# lst = list(set(lst))
# print(set(lst))
# print(type(set(lst)))

# s1 = {1, 2, 3}
# s2 = {3, 6, 9}
# print(s1|s2) # 합집합
# print(s1-s2) # 차집합
# print(s1&s2) # 교집합


# a, b = 0, -1
# print(bool(a), bool(b)) # False, True

# a1 = bool('a')
# b1 = bool('')
# c1 = bool('0')
# print(a1, b1, c1)

# a = True
# b = False
# c = True
# d = False

# print(1 or 0)   # '1'
# print(0 or -1)  # '-1'
# print(-1 or 1)  # '-1'

# print('a' and 'b')  # 'b'
# print('' and 'a')   # ''
# print(0 and 1)      # '0'

# print(a and b)  # False
# print(a and c)  # True
# print(a or b)   # True

a = 1
b = 0
c = 3

print(a or c)   # 1
print(a|c)      # 비트연산 or -> 3
print(b or c)   # 3
print(a and b)  # 0
print(a and c)  # 3
print(c and a)  # 1