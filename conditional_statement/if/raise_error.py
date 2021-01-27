# raise NotImplementedError
# 미구현 상태인 부분이 있을 때, 실행이 가능하게 해줌
# 오류를 발생시켜 구현되지 않았음을 알려줌

number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    # print("짝수")
    raise NotImplementedError
else:
    # print("홀수")
    raise NotImplementedError