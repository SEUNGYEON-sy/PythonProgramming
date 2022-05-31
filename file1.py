f = open("a.txt", "w")
f.write("반갑습니다")
f.close()

f = open("a.txt", "a")
f.write(" 안녕히계세요")
f.close()

f = open("a.txt", "r")
print(f.read())
