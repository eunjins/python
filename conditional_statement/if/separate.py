number = input("정수 입력> ")
number = int(number)

number = str(number)
last_character = number[-1]    # 마지막 자리 숫자 추출
last_number = int(last_character)

# 줄이 너무 길어질 것 같으면, \을 입력해 줄바꿈해서 코드를 입력
# 짝수인지 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수")

# 홀수인지 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9 :
    print("홀수")