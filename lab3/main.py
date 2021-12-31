grade = "-"
a = ["F", "D", "C", "B", "A", "+", "-"]
b = [0, 1, 2, 3, 4, 0.3, (-0.3)]
mark = 0
m=0
for char in grade:
    print(char)
    print(a.index(char))
    print(b[a.index(char)])
