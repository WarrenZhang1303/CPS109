"""
1
Write a function called helloWorld(), which prints "Hello World". Next write a program that
calls that function once. In the same program, add a loop which calls the function 10 times.
"""


def helloWorld():
    print("Hello World")


"""
2
Write a function hello(name), which prints "Hello" followed by the value of name. For
example, hello('Ahmad') would print "Hello Ahmad". Write a program that asks the user for
their name, and then uses the function to greet the person. 
"""


def hello(name):
    print("Hello", name)


"""
3
Write a function hello(firstname, lastname), which, for example, if called with hello('John',
'Smith'), would print two lines:
Hello John Smith
Hello Smith, John
Use the function in a program where you ask the user for first and last name and then call the
function.
"""


def hello(firstname="", lastname=""):  # give these two parameters a default values
    if lastname == "":  # Include Q2 answer
        print("Hello", firstname)
    else:
        print("Hello", firstname, lastname)
        print("Hello", lastname + ",", firstname)


"""
4
Write a function repeatPhrase(phrase, n), which prints the given phrase n times, alternating
between lowercase and uppercase. Recall, that if aString is a string, then a.upper() is the
uppercase of that string, and a.lower() is the lower case of the string. For example, repeat('The
sky is blue', 5) would print:
the sky is blue
THE SKY IS BLUE
the sky is blue
THE SKY IS BLUE
the sky is blue
Use the function in a program where you ask the user for the phrase and the value of n.
"""


def repeatPhrase(phrase, n):
    if n == 0:  # When the number of print times is zero, the recursion ends.
        pass
    elif n < 0:
        print("ERROR")
    elif n % 2 == 0:  # if the number of print times are even number, upper string
        print(phrase.upper())
        repeatPhrase(phrase, n - 1)  # the number of print times -1, continue recursion
    else:  # odd number
        print(phrase.lower())
        repeatPhrase(phrase, n - 1)


"""
5
Write a function timestable(n), which prints a multiplication table of size n. For example,
timestable(5) would print:
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
Use the function in a program where you ask the user for n and you print the corresponding
table.
"""


def timetable(n):
    if n <= 0:
        print("null")
    else:
        for i in range(1, n + 1):  # row
            for j in range(1, n + 1):
                target = str(i * j)
                print(target.zfill(len(str(n ** 2))), "  ", end="")
                """
                .zfill can fill zero before the number,
                zfill only support strings, num**2 is the largest number in table , 
                it also have the maximum number of digits.
                end = "" means print end with nothing (original print() have \n)
                """

            print("\n")  # when a row end, change to a new line


"""
6
 Write a function perfectcube(n), which returns True if n is a perfect cube and returns False
otherwise. Notice that this function is not printing anything, but rather returning True or False.
The function must use \nexhaustive enumeration\n to check if n is a perfect cube. That means
checking if 0**3 is n or 1**3 is n or 2**3 is n, and so on, up to where it is pointless to check
further. (Instead of n, you might be checking against abs(n), since for example, -125 is a perfect
cube. Use the function in a program where you ask the user for n and you print a statement like
"Yes, that is a perfect cube" or "No, that number is not a perfect cube", as appropriate.
"""


def perfectcube(n):
    pointer = 0
    while True:
        if pointer ** 3 > abs(n):  # not a perfect cube
            return False
        elif pointer ** 3 == abs(n):  # is a perfect cube
            return True
        else:
            pointer += 1


#   RECURSION CHALLENGE (Just for fun)
# def perfectcube(n, pointer=0):  # pointer a default parameter =0
#     if pointer ** 3 > abs(n):  # not a perfect cube
#         return False
#     elif pointer ** 3 == abs(n):  # is a perfect cube
#         return True
#     else:
#         return perfectcube(n, pointer + 1)  # n keep the same , pointer plus one , replete the function


"""
7
Write a function biggestOdd(), which reads in numbers from the user until the user enters 0.
Then the function returns (not prints) the largest odd number that was entered. For example, if
the integers were: 10, 9, 7, 12, 2, 5, 15, 100, 90, 60, 0, then the program would return 15 as the
largest odd number. Similarly, if the integers were -55, -33, -10, 100, -5, 0, then the program
would return -33 as the largest odd number. If there is no odd number, then the function should
return 0. Use the function in a program to check that it works.
"""


def biggestOdd():
    ans = 0
    while True:
        input_int = int(input("7) Please enter an integer: "))
        if input_int == 0:
            return ans

        if ans == 0 and input_int % 2 == 1:  # it only use once at beginning
            ans = input_int
        elif input_int % 2 == 1 and input_int > ans:  # it is odd number and bigger than the ans
            ans = input_int  # cover the old one


#   RECURSION CHALLENGE (Just for fun)

# def biggestOdd(ans=0):  # default parameter ans only store the biggest odd :|
#     input_int = int(input("Please enter an integer: "))
#     if input_int == 0:  # exit door
#         return ans
#     if ans == 0 and input_int % 2 == 1:  # it only use once at beginning
#         ans = input_int
#         return biggestOdd(ans)
#     elif input_int % 2 == 1 and input_int > ans:    # it is odd number and bigger than the ans
#         ans = input_int # cover the old one
#         return biggestOdd(ans)
#     else:
#         return biggestOdd(ans)  # change nothing, continue running


"""
8
Write a function biggestBuried(s), which the parameter s is a string, and the function returns
the largest integer buried in the string. If there is no integer inside the string, then return 0. For
example, biggestBuried('abcd51kkk3kk19ghi') would return 51, and
biggestBuried('kkk32abce@@-33bb14zzz') would return 33, since the '-' character is treated
like any other non digit. Note that a character is a digit if it is greater than or equal to '0' and
less than or equal to '9'. Alternatively, you can use string.isdigit() to check if the string is a
digit. Use the function in a program to test that it works properly by saying
print(biggestBuried('abcd51kkk3kk19ghi')) answer should be 51
print(biggestBuried('kkk32abce@@-33bb14zzz')) answer should be 33
print(biggestBuried('this15isast22ring-55')) answer should be 55
"""


def biggestBuried(s):
    for char in s:
        if not char.isdigit():
            s = s.replace(char, ",")  # if char is not a digital, replace it to be ","

    #   Now, only digit and "," in the string: ,,,,,51,,,,3,,,19
    s_list = s.split(",")  # split string with "," now, all digit numbers and "empty elements" are split in the list
    ans = []  # Use to store digital number without empty elements
    for i in range(len(s_list)):
        if len(s_list[i]) != 0:  # if it is not an empty element
            ans.append(int(s_list[i]))  # str-->int

    if len(ans) == 0:  # no digit number
        print(0)
    else:
        print(max(ans))  # max() find the largest integer in the list


"""
9
Write a function squareRoot(x, epsilon) that uses bisection search to return a number y that is
close enough to the square root of x, so that abs(y**2 - x) < epsilon. Try out the function in a
program to verify that it works properly. 
"""


def squareRoot(x, epsilon):
    low = 0.0
    high = max(1, x)  # if 0<x<1 high==1
    mid = (high + low) / 2.0
    if x < 0:
        return "none"
    elif x == 0:
        return 0
    else:
        while abs(mid ** 2 - x) >= epsilon:
            if mid ** 2 < x:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2.0
        return mid


"""
10
Write a function decimalToBinary(n) that converts a positive decimal integer n to a string
representing the corresponding binary number.
"""


def decimalToBinary(n):
    ans = ""  # it used to store the correct answer
    s = n  # copy one
    ram = []  # it used to store the reverse answer
    while s != 0:
        ram.append(s % 2)  # store the reminder
        s = s // 2
    for i in range(len(ram)):
        ans += str(ram[len(ram) - 1 - i])  # int-->str; Traverse the list, output in reverse order
    print(n, "is the binary of", ans)


#   RECURSION CHALLENGE (Just for fun)

# def decimalToBinary(n, ram=[], ans=""):
#     if n == 0 and len(ram) == 0:
#         return 0
#     elif n == 0 and len(ram) != 0:
#         for i in range(len(ram)):
#             ans += str(ram[len(ram) - 1 - i])
#         return ans
#     else:
#         ram.append(n % 2)
#         return decimalToBinary(n // 2)


if __name__ == '__main__':
    # Q1
    helloWorld()
    print("-------")
    for i in range(0,10):
        helloWorld()

    # 02
    name = input("2) What's your name?: ")
    hello(name)

    # 03
    firstname = input("3) What's your firstname?: ")
    lastname = input("What's your lastname?: ")
    hello(firstname,lastname)

    # 04
    input_string = input("4) Please enter something: ")
    input_integer = int(input("How many times?: "))
    repeatPhrase(input_string, input_integer)

    # 05
    timetable_input = int(input("5) Please enter an integer: "))
    timetable(timetable_input)

    # 06
    user_input = float(input("6) Please input an integer to check if it has a perfect cube:"))
    print(perfectcube(user_input))

    # 07
    print(biggestOdd())

    # 08
    s_input = input("8) Please enter an string:")
    biggestBuried(s_input)

    # 09
    x = float(input("9) Please enter an positive number to find it square root: "))
    epsilon = float(input("Please enter the epsilon"))
    print(squareRoot(x, epsilon))

    # 10
    user_input = int(input("10) Please enter a positive integer: "))
    decimalToBinary(user_input)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
