# # Set 관련 메소드
# # set (중복을 허용하지 않는 데이터들의 묶음)
# s = {1,2,3,4,5}
# # 값 추가
# s.add(6)
# s.update([11,12,13,14])
# # 값 삭제
# s.remove(6) # 없는 값 삭제시 오류
# s.discard(16) # 오류는 안남
# s.clear() # 전체 다 삭제

# # 집합표현
# s1 = {1,2,3,4,5}
# s2 = {2,4,6,8}
# # 교집합
# print(s1&s2)
# print(s1.intersection(s2))
# # 합집합
# print(s1|s2)
# print(s1.union(s2))
# # 차집합
# print(s1-s2)
# print(s1.difference(s2))
# # 부분집합
# # s1의 모든 항목이 s2에 들어가 있으면 True 반환
# print(s1<=s2)
# print(s1.issubset(s2))
# # s1이 s2의 모든 항목을 포함하고 있다면 True 반환
# print(s1>=s2)
# print(s1.issuperset(s2))



# # 딕셔너리
# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# # 딕셔너리 값 출력
# print(st['kevin']) # 없는 키를 입력하면 에러가 남
# print(st.get('kevin', '없는key입니다.')) # 없는 키를 입력해도 에러가 안남(default : None)
# # 딕셔너리에 값 추가하기 [방법1]
# st['kate'] = 'hi'
# print(st)
# st['kevin']=11 # 딕셔너리는 중복되는key 값을 가질 수 없다.
# print(st)
# # 딕셔너리에 값 추가하기 [방법2]
# st.update(camel=11)
# print(st)
# st.update(kevin=100)
# print(st)
# st.update(even=200, faker = 300)
# print(st)
# dict2 = {'fly' : 201, 'amy' : 301}
# st.update(dict2)
# print(st)

# # 방법1
# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# ls_key = ['asdf', 'zcv', 'qwe']
# ls_value=[1,2,3]
# st.update(dict(zip(ls_key, ls_value)))
# print(st)
# # 방법2
# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# ls_key = ['asdf', 'zcv', 'qwe']
# ls_value=[1,2,3]
# for i in range(3) : 
#     st.update({ls_key[i]:ls_value[i]})
# print(st)
# # 방법3
# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# ls_key = ['asdf', 'zcv', 'qwe']
# ls_value=[1,2,3]
# for i in range(3) : 
#     st[ls_key[i]] = ls_value[i]
# print(st)
# # 방법4
# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# ls_key = ['asdf', 'zcv', 'qwe']
# ls_value=[1,2,3]
# for i in range(3) : 
#     st.setdefault(ls_key[i], ls_value[i])
# print(st)
# # 원본 데이터에 추가하려는 데이터와 같은 키가 존재한다면 원본 데이터 보호(같은 키는 추가 안됨)
# st.setdefault('amy','korea')
# st.setdefault('kevin','USA')
# print(st)


# # 딕셔너리 값 삭제
# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# del st['kevin'] # 없는 키 삭제 시도 -> 에러 발생 # 굳이 따지자면 pop보다 수행속도가 미세하게 빠름
# print(st)
# st.pop('kevin', '없음') # 2번째 인자값(반환값) 추가 -> 에러 발생 X
# print(st)

# st = {'kevin' : 1, 'john' : 2, 'bob' : [3,4,5]}
# lst = st.keys()
# print(lst)
# print(list(lst))
# lst = st.values()
# print(lst)
# print(list(lst))
# lst = st.items()
# print(lst)
# print(list(lst))



# # collection 모듈에서 counter 라는 클래스 이용하기
# from collections import Counter
# lst = ['apple', 'mango', 'banana', 'mango', 'apple', 'mango', 'banana', 'mango', 'apple']
# print(Counter(lst))
# ret = dict(Counter(lst))
# print(ret)

# print(Counter('an applemango'))
# st = 'an applemango'
# # st 문자열에서 가장 많이 사용된 알파벳 출력해주세요.
# ret2 = dict(Counter(st))
# ret2 = sorted(ret2.items(),key=lambda x:x[1], reverse=True)
# print(ret2)
# print(ret2[0][0])

# ret3 = Counter(st).most_common(1)
# print(ret3[0][0])

# a = Counter('apple')
# b = Counter('mango')
# print(a+b)
# print(a-b)


# '''
# DAT(Direct Address Talbe) 
# 배열 안의 값을 다른 배열의 인덱스로 사용
# lst = [4,7,1,8,5,9,1,4,7]
# mc = [4,7,1,8,5]
# 원래 45번 탐색하는데 14번 탐색으로 가능
# //
# 바이너리 서치
# //
# 해쉬

# '''

# print(hash('a'))
# print(hash('김희주'))
# print(hash([3,4,5,6])) # 불변의 값이 아닌 변경 가능한 값들은 해쉬의 key값으로 사용 불가
# print(hash(3,4,5,6)) # 튜플(불변이니까)은 가능