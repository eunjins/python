# 문자열, 연산자

print("큰따옴표")
print('작은따옴표')

print('"큰따옴표"를 내부에 넣고 싶다면 작은따옴표로 문자열을 만든다.')
print("'작은따옴표'를 넣고 싶다면 큰따옴표로 문자열을 만든다.")

# 이스케이프 문자를 사용하면 문자 그대로 인식
print("\"큰따옴표\"")
print("\'작은따옴표\'")
print("\\이스케이프")

# 여러 줄 문자열
print("""hello
python
!!!""")

# 연결
print("hello, " + "python")

# 반복
print("hello, " + "python " * 3)

# 문자 선택
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

# 문자 선택 (음수)
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

# 범위 선택
print('"안녕하세요"[0:2]:', "안녕하세요"[0:2])  # index 0~1
print('"안녕하세요"[1:3]:', "안녕하세요"[1:3])  # index 1~2
print('"안녕하세요"[1:4]:', "안녕하세요"[1:4])  # index 1~3

print('"안녕하세요"[3:]:', "안녕하세요"[3:])
print('"안녕하세요"[:3]:', "안녕하세요"[:3])

# 길이 및 타입 구하기
hello = "안녕하세요"
length = len(hello)

print(len(hello))
print(len)
print(type(hello))
print(type(len(hello)))
print(type(len))

# 제곱 연산자
a1 = 2 ** 2
a2 = 2 ** 4
print("a1 = ", a1)
print("a2 = ", a2)