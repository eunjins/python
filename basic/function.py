# Function without parameters
def print_hello():
    for i in range(3):
        print("hello")

print_hello()

# Functions containing parameters
def print_value(value, n):
    for i in range(n):
        print(value)

print_value("hi", 3)

'''
가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
가변 매개변수는 하나만 사용할 수 있다.
'''
# 가변 매개변수
def print_values(n, *values):
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        print("-----")

print_values(3, "abc", "def", "g", "hijk")

'''
기본 매개변수 뒤에는 일반 변수가 올 수 없다.
'''
# 기본 매개변수
def print_n_times(value, n=3):
    # n번 반복
    for i in range(n):
        print(value)

print_n_times("n")