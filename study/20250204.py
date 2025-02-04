# class Plusminus : 
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def plus(self) : 
#         result = self.first + self.second
#         return result
#     def minus(self) : 
#         result = self.first - self.second
#         return result

# # 하위 클래스를 하나 생성
# # 숫자 3개의 곱을 생성해주는 하위 클래스
# class MoreFunction(Plusminus) : 
#     def __init__(self, first, second, third) : 
#         super().__init__(first, second) # 부모 클래스의 init 메서드를 그대로 호출하는 경우
#         self.third = third

#     def multi(self) : 
#         result = self.first * self.second * self.third
#         return result
    
#     def plus(self) : 
#         result = self.first + self.second + self.third
#         if result > 100 :
#             return print('버그')
#         else : 
#             return print(result)

#     def parents_plus(self) : 
#         ret = super().plus()
#         return ret

# test = MoreFunction(400, 500, 200)
# print(test.parents_plus())

# b = MoreFunction(3, 4, 5)
# print(b.multi())
# b.plus() # 자식클래스의 인스턴스로 부모클래스의 메서드 접근 가능

# # 부모클래스의 plus 메소드를 자식클래스에서 수정하고자 한다
# # plus 메서드는 숫자 2개가 아닌 숫자 3개의 합을 출력하는 메서드로 바꾸고
# # 만약 숫자의 합이 100이 넘는다면 '버그'라고 출력이 되도록 수정해보자

# a = MoreFunction(1,1,999)
# a.plus()


# # 메서드 오버로딩
# # 클래스 내부에 같은 이름의 여러 메서드를 정의

# # 메서드 오버라이딩
# # 동일한 메서드가 클래스에서 따라 다르게 행동할 수 있음

# # 다형성 : 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다는 뜻(ex : 메서드 오버라이딩)

# # 상속 : 자식클래스가 부모클래스로부터 메서드 또는 속성 등을 상속받아서 사용

# # 추상화 : 공통의 속성이나 기능을 묶어 상위 클래스에 구현, 하위객체에는 각각 객체의 고유 기능만 추가

# # 캡슐화 : 클래스 내 객체(속성 또는 메서드)를 외부에서 수정하지 못하도록 막는 것
#     # public
#     # protected -> "암묵적 규칙"에 의해 메서드를 호출 시 부모클래스 내부나 자식클래스에서만
#         # '_' <- 매개변수 앞에 언더바 하나
#     # private
#         # '__' <- 매개변수 앞에 언더바 두개

# class Person : 
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         # self.__age = age
#     def getage(self) : 
#         return self._age
#         # return self.__age
    
# p1 = Person('김희주', 50)
# print(p1.name) # 김희주
# # print(p1._age)
# print(p1.getage()) # 50

# #print(p1.__age)
# print(p1.getage()) # 50



# class Person :
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
    
#     @property                       # getter 함수 위에는 @property라고 적어주고
#     def age(self) :                 # 비공개 속성의 값을 읽기 위한 용도로 사용한다.
#         return self.__age
    
#     @age.setter                     # @메서드명.setter라고 적어준다
#     def age(self, value) :          # 비공개 속성의 값을 변경하기 위한 용도로 사용한다.
#         self.__age = value

# k = Person('김규리', 25)
# print(k.age)    # 25    getter 
# k.age = 20
# print(k.age)    # 20    setter


# if True : 
#     print('참')
# else : 
#     print('거짓')

# # SyntaxError : invalid syntax

# print('hi)
      
# # SyntaxError : EOL while scanning string literal

# a = 10* (1/0)

# # ZeroDivisionError : division by zero

# print(abc)

# # NameError: name 'abc' is not defined

# a = 1 + '1'

# # TypeError

# a = round('3.5')

# # TypeError

# import random
# random.sample([1, 2, 3])

# # TypeError: sample() missing 1 required positional argument: 'k'

# a = int('3.5')

# # ValueError

# numbers = [1, 2]
# numbers.index(3)

# #ValueError

# empty_list = []
# empty_list[-1]

# # IndexError : list index out of range

# songs = {'new jeans' : 'supershy'}
# songs['ive']

# # KeyError: 'ive'

# import reque

# # moduleNotFoundError : Nomodule named 'reque'

# for i in range(3) : 
# print(i)

# IndentationError