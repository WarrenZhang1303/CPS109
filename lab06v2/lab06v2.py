import builtins
import random
import math

"""
Q1
Write a program that has a loop to read in ten strings and put them into a list.
Write a second loop to print the strings in the reverse order.
This is an exercise in indexing, so do not use the reverse() method of list.
Print the index in the following format.
"""


def reverse_order():
    l = []  # create a empty list named 'l' to store user inputs

    def q1_input():  # Helper function 1 :Responsible for store the user inputs
        for i in range(10):
            print("Enter string", i, end="")
            user_input = input("/10: ")
            l.append(user_input)
        return q1_output()

    def q1_output():  # Helper function 2 : Only responsible for print out the usr_inputs
        # (reverse_order)
        for i in range(len(l)):
            print("String", len(l) - 1 - i, end="")
            print("/10:", (l[len(l) - 1 - i]))

    return q1_input()  # <-- entrance here


"""
Q2
Write a function max(L) which examines the argument list L, 
and returns the largest object of type float. 
If there is no float object in the list, then the function returns None. For example,
max([100, 'blue', 3.5, 'sugar on the rocks', 7.0]) would return 7.0, and
max([7, 2, 9, 1]) would return None.
Note that type(element) == float is a way to check if element is a float.
"""


def max(L):  # what a bad function name :(
    ans = []

    def find_float(L):  # helper function: pick all the floats from L and put them in the ans list
        for i in range(len(L)):
            if type(L[i]) == float:
                ans.append(L[i])
        return find_max(ans)

    def find_max(a):  # helper function: find the max elements in the "ans"
        if len(a) == 0:
            return None
        else:
            return builtins.max(a)  # import specific max() method from python

    return find_float(L)


"""
#3
Write a function longest(L) which examines the argument list L and returns the longest string. 
You can assume all of the elements of the list L are strings,
 and that the list is not empty.
Use the approach where there is a variable largestyet which is initialized to the first element of L. 
Then go through the rest of the elements and 
update largestyet whenever you encounter a longer string. 
For example, longest(['blue', 'red', 'the old barn', 'the white house', 'green']) 
would return 'the white house'.
"""


def longest(L):
    largestyet = L[0]
    for i in range(len(L)):
        if len(L[i]) > len(largestyet):
            largestyet = L[i]
    return largestyet


"""
#4
Write a program that makes both a list L and a tuple T with the following values: 
a) the numbers 1 to 100, inclusive.
b) the odd numbers from 1 to 101, inclusive.
c) the squares of numbers from 0 to 49, inclusive
d) 60 random integers from 0 to 49, where you import random and use random.randrange(0, 50) to give each value.
e) 50 zeroes, i.e., [0, 0, ...., 0] and (0, 0, ..., 0). 
Note, you can use repetition, as you would for a string. 
Do not use list comprehension for this question.
Print each list and tuple using print(L) and print(T).
"""


# a) the numbers 1 to 100, inclusive.
def list_was_tuple():
    L = []
    T = ()
    for i in range(1, 101):
        L.append(i)

    # b) the odd numbers from 1 to 101, inclusive.
    for i in range(1, 102):
        if i % 2 == 1:
            L.append(i)

    # c) the squares of numbers from 0 to 49, inclusive
    for i in range(50):
        L.append(i ** 2)

    # d) 60 random integers from 0 to 49,
    for i in range(60):
        L.append(random.randrange(0, 50))

    # e) 50 zeroes
    for i in range(50):
        L.append(0)
    # Copy to tuple
    for i in range(len(L)):
        T = T + (L[i],)

    print(L)
    print(T)



"""
#5
"""
def list_comprehension():
    # a) the numbers 1 to 100, inclusive.
    L = [x for x in range(1, 101)]

    # b) the odd numbers from 1 to 101, inclusive.
    L = L + [x for x in range(1, 102) if x % 2 == 1]

    # c) the squares of numbers from 0 to 49, inclusive
    L = L + [x ** 2 for x in range(0, 50)]

    # d) 60 random integers from 0 to 49
    L = L + [random.randrange(0, 50) for x in range(0, 60)]

    # e) 50 zeroes
    L = L + [0 for i in range(0, 50)]
    print(L)


"""
#6
Write a function perimeter(poly) which
finds the perimeter of a polygon, where the input argument poly is a list of tuples,
each tuple being the (x, y) coordinates of a point on the polygon. 
The perimeter is the sum of the distances from one point to the next, including the distance from the last point to the first.
The distance between (x1, y1) and (x2, y2) is
sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
"""


def perimeter(poly):
    p_len = len(poly)
    ans = 0
    for i in range(len(poly)):
        x2_x1 = (poly[p_len - 1 - i][0] - poly[p_len - 2 - i][0]) ** 2
        y2_y1 = (poly[p_len - 1 - i][1] - poly[p_len - 2 - i][1]) ** 2
        line = math.sqrt(x2_x1 + y2_y1)
        # ans=ans+ math.sqrt((poly[p_len-1-i][0]-poly[p_len-2-i][0])**2+(poly[p_len-1-i][1]-poly[p_len-2-i][1])**2)
        ans += line

    print(ans)

"""
#7
"""

def permutation(L):
    P = []
    C = list(L)

    def nonename(C):
        if len(C) != 0:
            i = random.randrange(0, len(C))
            P.append(C.pop(i))
            return nonename(C)
        else:
            return P

    return nonename(C)


if __name__ == '__main__':
    # 1
    reverse_order()
    # 2
    print(max([100, 'blue', 3.5, 'sugar on the rocks', 7.0, "8.9", 8.9]))
    # 3
    print(longest(['blue', 'red', 'the old barn', 'the white house', 'green']))
    # 4
    list_was_tuple()
    # 5
    list_comprehension()
    # 6
    poly = ((1, 3), (2, 5), (4, 4))
    perimeter(poly)

    # 7
    L = [(0, 0), (20, 0), (20, 10), (0, 10)]
    A = [19, 4, 3, 17]
    for i in range(2):
        print(permutation(A))

    print(random.sample(L, len(L)))
