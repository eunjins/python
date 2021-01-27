# 존재하지 않는 키에 접근하고 있는 경우 대처 방법 2
# <dictionary>.get(<key>)

dictionary = {
    "name": "망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("value: ", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")