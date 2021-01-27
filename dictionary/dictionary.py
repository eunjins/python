# string == key
# dictionary: { }로 선언

# {
#   <key>: <value>,
#   <key>: <value>,
#   ...
#   <key>: <value>
# }

dictionary = {
    "name": "망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "나트륨", "치자황색소"],
    "origin": "필리핀"
}

print(dictionary)

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("origin: ", dictionary["origin"])
print()

# change value
dictionary["name"] = "건조 망고"
print("name: ", dictionary["name"])
