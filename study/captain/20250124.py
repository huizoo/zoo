# st = 'apple,banana,mango'

# index=st.find('p') # 없는거면 -1
# print(index)

# index2=st.index('p') # 없는거면 오류
# print(index2)

# print(st.isupper()) # 모두 대문자인지
# print(st.islower()) # 모두 소문자인지
# print(st.isalpha()) # 모두 알파벳인지


# print(st.count('a')) # 'a' 개수 카운트


# # 리스트 안의 문자열을 한 문자열로 만들때 사용
# st = ['a', 'p', 'p', 'l', 'e',]
# ret=" ".join(st) # "" - 구분자
# print(ret)


# # 리스트 안에 문자를 합치는데 사이에 ,를 넣어라
# st =['apple', 'banana', 'mango']
# st2 = ",".join(st)
# print(st2)

# st3 = 'apple,banana,mango'
# st4 = st3.upper() # 전부 대문자로
# print(st4)
# st5 = st4.lower() # 전부 소문자로
# print(st5)


# st = '   apple'
# print(st)         # 왼쪽 공백 제거 : lstrip()
# st2 = st.lstrip() # 오른쪽 공백 제거 : rstrip()
# print(st2)        # 전체 공백 제거 : strip()


# st = 'apple'
# print(st[0])
# st2=st.replace('ap', 'ma')
# print(st2, st)


# st = 'apple'
# print(reversed(st))
# print(list(reversed(st)))
# print("".join(list(reversed(st))))
# print(st[::-1])


'''
리스트 관련 메소드
'''
# # append
# st = ['apple', 'banana', 'mango']
# st.append('orange')
# print(st)
# st.append('orange')
# print(st)

# # insert
# st.insert(1, 'strawberry')
# print(st)

# # index
# a = st.index('orange')
# print(a)

# # extend
# st = [1, 2, 3]
# st2 = [4, 5]
# # st += st2
# st.extend(st2)
# print(st)

# pop, remove, del, clear
# st = [1, 2, 3, 4, 5]
# ret = st.pop() # pop은 괄호 안에 비어있으면 맨 뒤 삭제 및 반환
# print(st)
# print(ret)

# ret2 = st.remove(3) # remove는 반환값 없음 
# print(st)
# print(ret2)

# del st[1:] # 해당 인덱스부터 끝까지 삭제
# print(st)

# st.clear() # 리스트 내부 요소 전부 삭제
# print(st)


# # reverse 뒤집는것
# st=[1, 2, 3, 4, 5]
# st.reverse()
# print(st)
# st=st[::-1]
# print(st)


# # sort 정렬하는것

# a1=[6, 3, 9]
# print(a1)
# a1.sort()
# print(a1)
# a1=[6, 3, 9]
# print(sorted(a1))
# ret=sorted(a1, reverse=True) # 내림차순변경
# print(ret)


# a1 = 'asdf'
# str2 = sorted(a1)
# print(str2)
# print(' '.join(str2))


# lst=list(range(1,11))

# print(sorted(lst, reverse=True))

# ret=sorted(lst, key=lambda x: -x) # lambda를 써도 적용됨

# print(ret) # 1. 홀수 우선, 내림차순 이런걸 lambda형태로 할 수도 있음


# lst = ['apple', 'mango', 'banana']

# ret = sorted(lst, reverse=True) # lambda 는 숫자로 가능하지만 문자열은 reverse=True를 써야함함
# print(ret)

# lst -> iterable 객체
# key -> 정렬을 할 기준
# reverse = True -> 내림차순
# 문자열은 lambda 의 리턴값으로 음수 불가


lst = [(3, 'banana'), (2, 'apple') ,(1, 'carrot')]
#문자열 내림차순 기준으로 정렬 후 출력
ret = sorted(lst, key = lambda x : x[1], reverse = True)
print(ret)