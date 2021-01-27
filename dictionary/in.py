# 존재하지 않는 키에 접근하고 있는 경우 대처 방법 1
# <key> in <dictionary>

dictionary = {
    "name": "망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "나트륨", "치자황색소"],
    "origin": "필리핀"
}

if "존재하지 않는 키" in dictionary:
    print(dictionary["존재하지 않는 키"])
else:
    print("KeyError: 존재하지 않는 키에 접근하고 있습니다.")