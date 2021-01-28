f = open("test.txt", "w")
f.write("hello")
f.close()

f = open("test.txt", "r")
line = f.readline()
print(line)
f.close()