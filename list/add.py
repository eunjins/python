# 원본 리스트에 직접적인 영향을 줌
# append(<요소>): 뒤에 추가
# insert(<위치>, <요소>): 중간에 추가
# extend(<리스트>): 뒤에 리스트 추가

# append()
a = [1, 2, 3]

a.append(4)
a.append(5)
print(a)
print()

# insert()
a.insert(0, 10)
print(a)

# extend() example_1
b = [7, 8, 9]
b.extend(a)
print(b)

# extend() example_2
b.extend([3, 6, 0])
print(b)