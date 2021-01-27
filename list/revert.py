# list revert keword & function

a = [0, 1, 2, 3, 4, 5]
print(a)

## 1. del
del a[1]
print(a)

## 2. pop(<제거할 위치>)
a.pop(2)
print(a)
print()
# pop(): 매개변수 입력하지 않으면 자동으로 -1이 들어감 (마지막 요소 제거)

## 여러 개 제거
b = [0, 1, 2, 3, 4, 5, 6, 7]
print(b)
del b[3:6]
print(b)
print()

## 3. remove(<value>)   # 리스트의 특정 값 제거
c = [1, 2, 1, 2]
print(c)
c.remove(2)
print(c)
print()

## 4. <list>.clear()
d = [0, 1, 2, 3, 4, 5]
print(d)
d.clear()
print(d)
