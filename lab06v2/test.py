import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def test01 ():
    t1 = (1, 'two', 3)
    t2 = (t1, 3.25)
    print(t2)
    print(t1 + t2)
    print((t1 + t2)[3])
    print((t1 + t2)[2:5])

def person(name, age, *what, **kw):
    print(name)
    print(age)
    print(what)
    print(kw)

if __name__ == '__main__':
    # test01()
    # print_hi('Warren')
    # person("Hello", 20, "w", y=4, x="ee")
    t=[]
    L=[]
    L = L + [random.randrange(0, 50) for i in range(0, 60)]
    # L = L + [0 for i in range(0, 50)]
    print(L)
    print(len(L))