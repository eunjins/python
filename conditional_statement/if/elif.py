number = input("정수 입력> ")
number = int(number)

if 0 <= number < 10:
    print("0 ~ 9")
elif 10 <= number < 20:
    print("10 ~ 19")
elif 20 <= number < 30:
    print("20 ~ 29")
elif 30 <= number < 40:
    print("30 ~ 39")
else:
    print("40 ~")