# 숫자 -> 문자
a = "{}".format(52273)
print(type(a), a)

format_a = "{}원".format(1000)
format_b = "{} {} {}".format(1, 2, 3)
format_c = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)

# 특정 칸에 출력
x = "{:d}".format(52)
y = "{:5d}".format(52)      # 5칸
z = "{:10d}".format(52)     # 10칸

# 빈 칸 0으로 채우기
d = "{:05d}".format(52)     # 양수
e = "{:05d}".format(-52)    # 음수

print("# 기본")
print(x)
print("# 특정 칸에 출력")
print(y)
print(z)
print("# 빈 칸 0으로 채우기")
print(d)
print(e)
print("---------")

# 기호와 출력
f = "{:+d}".format(52)  # 양수
g = "{:+d}".format(-52) # 음수
h = "{: d}".format(52)  # 양수: 기호 부분 공백
i = "{: d}".format(-52) # 음수: 기호 부분 공백

print(f)
print(g)
print(h)
print(i)