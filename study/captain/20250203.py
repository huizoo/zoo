# class Calculator():
#     numberOFCalcul = 0        # 모든 인스턴스가 같이 사용할 변수 -> 클래스 변수
#     def __init__(self):     # '__' 들어간 것은 매직메서드 중 __init__ 생성자함수(contructor)
#         self.result = 0       # 각각의 인스턴스를 위한 변수 -> 인스턴스 변수(속성)
#         Calculator.numberOFCalcul += 1

#     def getsum(self,value):
#         self.result+=value
#         return self.result

# cal1=Calculator() # 인스턴스 -- Calculator 클래스의 객체
# print(cal1.result) # 0
# cal1.getsum(3)
# print(cal1.result) # 3
# cal1.getsum(4)
# print(cal1.result) # 4
# cal1.getsum(5)
# print(cal1.result) # 5

# cal2=Calculator()
# print(cal2.result) # 0

# # ---
# cal1 = Calculator()
# print(cal1.numberOFCalcul) # 1
# cal2 = Calculator()
# print(cal2.numberOFCalcul) # 2


# Calculator.numberOFCalcul = 6
# print(cal1.numberOFCalcul) # 6
# print(cal2.numberOFCalcul) # 6

# # 주의점!!
# # 클래스 변수의 값을 바꿀 시 반드시 클래스로 접근해서 값 변경해야 함!!
# # 예시 > Calculator.numberOFCalcul = 6 (line 30)

# cal1.numberOFCalcul = 20        # 인스턴스로 클래스 변수값 바꿈(잘못된 예)
# Calculator.numberOFCalcul = 10
# print(cal1.numberOFCalcul)      # 20
# print(cal2.numberOFCalcul)      # 10


# class PlusMinus:
#     # def data(self, first, second) :
#     #     self.first = first
#     #     self.second = second

#     def __init__(self, first, second) : 
#         self.first = first
#         self.second = second

#     def plus(self) : 
#         result = self.first + self.second   
#         return result

#     def minus(self) : 
#         result = self.first - self.second
#         return result

# # a = PlusMinus()
# # a.data(3, 5)

# a = PlusMinus(3, 5)

# print(a.plus())
# print(a.minus())


# class car : 
#     def __init__(self, name, price) : 
#         self.name = name
#         self.price = price

#     def __add__(self, another) : 
#         return self.price + another.price
    
#     def __str__(self) : 
#         return f"{kia.name} 의 가격은 {kia.price}입니다."

# kia = car('k8', 300)
# bmw = car('m5', 500)
# print(kia.price + bmw.price) # 800

# print(kia+bmw)

# print(kia)

# del kia


# def deco(func):
#     def wrapping(value):
#         print('우유빛깔')
#         func(value)
#         print('화이팅')
#     return wrapping

# @deco
# def call_name(name):
#     print(name)

# @deco
# def call_age(age):
#     print(age)

# call_name('김희주')
# call_age('29')


# class car : 
#     def __init__(self, name, price) : 
#         self.name = name
#         self.price = price

#     @staticmethod
#     def add_price(one, another):
#         print(one+another)

# kia = car('k8', 300)
# bmw = car('m5', 500)

# car.add_price(500, 700)


# class Makepies:
#     cnt = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Makepies.cnt += 1
    
#     @classmethod
#     def number_of_pies(cls) : 
#         print(f'파이를 {cls.cnt}명이 만들고 있습니다.')

#     @classmethod
#     def from_birthday_year(cls, name, birthyear) :
#         age = 2025 - birthyear # 현재 연도를 기준으로 나이를 계산
#         return cls(name, age)

# a = Makepies('kevin', 40)
# b = Makepies('jane', 35)

# Makepies.number_of_pies()

# # class 변수 사용하는 경우
# # 1. 클래스로 클래스변수에 접근하고자 하는 경우
# # 2. 클래스 내 생성자함수를 대체해서 인스턴스를 생성할 때

# c = Makepies.from_birthday_year('bob', 1990)
