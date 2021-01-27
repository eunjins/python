# 사용자 입력 받을 때 input()
string = input("입력> ")
print(string)
print()

# input()의 결과는 무조건 문자열 자료형
# <class 'str'>
print("자료형: ", type(string))
print()

# 자료형변환
# 문자열을 숫자로 변환
i = int("12")
f = float("12.345")
print(type(i), i)
print(type(f), f)

# input()과 float() 조합
a = float(input("숫자 입력> "))
b = float(input("숫자 입력> "))

print("+: ", a + b)
print("-: ", a - b)
print("*: ", a * b)
print("/ ", a / b)
print()

# 숫자를 문자열로 변환
c = str(12)
d = str(12.345)
print(type(c), c)
print(type(c), c)