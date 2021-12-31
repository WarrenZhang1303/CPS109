# 1
# number>0 : number is positive;
# number< 0: number is negative;
# other situation is zero
def question_1(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


# 2
# list "room" stores all possibilities.
# variable "noun" responsible for the number's positive and negative
# variable "adj" responsible for the adjective
def question_2(number):
    noun = 0
    adj = 4
    room = ["zero", "positive", "negative", "large ", "small "]
    if number > 0:
        noun = 1
    elif number < 0:
        noun = 2
    if abs(number) > 1000:
        adj = 3
    elif abs(number) < 1:
        adj = 4
    else:
        return print(room[noun])
    return print(room[adj] + room[noun])


# 3
def question_3(integer):
    if integer % 1 != 0:  # to ensure that the entered value must be an integer
        return print("Please input an  integer.")
    if integer < 0:
        integer *= -1
    if integer >= 1000000:
        print("lots")
    elif integer >= 100000:
        print("6 digits")
    elif integer >= 10000:
        print("5 digits")
    elif integer >= 1000:
        print("4 digits")
    elif integer >= 100:
        print("3 digits")
    elif integer >= 10:
        print("2 digits")
    else:
        print("1 digit")


# 4
# n1=a n2=b n3=c
def question_4(n1, n2, n3):
    if n1 == n2:
        if n1 == n3:  # a==b==c
            print("All the same")
        else:  # a==b!=c
            print("Neither")
    elif n1 == n3:  # a==c!b
        print("Neither")
    elif n2 == n3:  # b==c!=a
        print("Neither")
    else:  # a!=b!=c
        print("All different")


# 5
def question_5(n1, n2, n3):
    if n1 == n2:  # 4，4，3/ 4，3，4 /4，3，3
        print("Neither")
    elif n1 == n3:
        print("Neither")
    elif n2 == n3:
        print("Neither")
    else:
        if n1 > n2 > n3:
            print("Decreasing")
        elif n1 < n2 < n3:
            print("Increasing")
        else:  # 4，6，5
            print("Neither")


# 6
def question_6(mode, n1, n2, n3):
    if mode == 0:  # strict mode
        if n1 == n2:
            print("Neither")
        elif n1 == n3:
            print("Neither")
        elif n2 == n3:
            print("Neither")
        else:
            if n1 > n2 > n3:
                print("Decreasing")
            elif n1 < n2 < n3:
                print("Increasing")
            else:
                print("Neither")
    elif mode == 1:  # lenient mode
        if n1 == n2:
            if n1 == n3:  # Exp: 1,1,1
                print("both increasing and decreasing")
            else:  # Exp:1,1,2 & 2,2,1
                if n1 > n3:
                    print("decreasing")
                else:
                    print("increasing")
        elif n1 == n3:  # 1,3,1
            print("Neither")
        elif n2 == n3:
            if n1 > n2:  # 2,1,1
                print("decreasing")
            else:  # 1,2,2
                print("increasing")
        else:
            if n1 > n2 > n3:
                print("Decreasing")
            elif n1 < n2 < n3:
                print("Increasing")
            else:
                print("Neither")
    else:  # Wrong input situation
        print("WRONG MODE! PLEASE TRY AGAIN!")


# 7
def question_7(n1, n2, n3):
    if n1 == n2:
        if n1 == n3:  # Exp: 1,1,1
            print("not in order")
        else:  # Exp:1,1,2 & 2,2,1
            print("in order")
    elif n1 == n3:  # 1,3,1
        print("not in order")
    elif n2 == n3:
        print("in order")
    else:  # Exp:3,2,1 & 1,2,3
        if n1 > n2 > n3 or n1 < n2 < n3:
            print("in order")
        else:
            print("not in order")


# 8
def question_8(n1, n2, n3, n4):
    if n1 == n2 and n3 == n4:  # Exp: 4,4,4,4 & 2,2,4,4
        print("two pairs")
    elif n1 + n2 == n3 + n4:  # Exp: 2,3,3,2 or 2,3,1,5
        if n1 == n3 or n2 == n3:  # make sure 2,3,1,5 is false
            print("two pairs")
        else:
            print("not two pairs")
    else:  # Exp 1,2,3,4
        print("not two pairs")


# 9
def question_9(scalar, temp):
    if scalar == 0:  # Celsius
        if temp >= 100:
            print(temp, " C " + "Water is gaseous.")
        elif temp <= 0:
            print(temp, " C " + "Water is solid.")
        else:
            print(temp, " C " + "Water is liquid.")
    elif scalar == 1:  # Fahrenheit
        if temp >= 212:
            print(temp, " F " + "Water is gaseous.")
        elif temp <= 32:
            print(temp, " F " + "Water is solid.")
        else:
            print(temp, " F " + "Water is liquid.")
    else:  # Wrong input situation
        print("WRONG MODE! PLEASE TRY AGAIN!")


# 10
# Letters and scores are stored separately, but the positions correspond to each other。
# letter_grade.index(char): the position of letter in the list.
# number_grade[letter_grade.index(char)]: the number on letter_grade.index(char) position.
def question_10(grade):
    letter_grade = ["F", "D", "C", "B", "A", "+", "-"]
    number_grade = [0, 1, 2, 3, 4, 0.3, (-0.3)]
    mark = 0
    for char in grade:
        mark += number_grade[letter_grade.index(char)]
    print("The numeric value of ", grade, "is", mark)


def question_11():
    sum = 0
    for i in range(100 + 1):  # 0~(99+1)
        if i % 2 == 0:
            sum += i
    print(sum)


def question_12():
    sum = 0
    for i in range(100 + 1):
        sum += i * i
    print(sum)


# 13
def question_13():
    for i in range(20 + 1):
        print("2**", i, "= ", 2 ** i)


# 14
def question_14(a, b):
    if a > b:
        print("ERROR!")
    else:
        sum = 0
        for a in range(b + 1):
            if a % 2 == 1:
                sum += a
        print(sum)


# 15
def question_15(number):
    sum = 0
    list = []
    letter = str(number)  # integer --> string

    for char in letter:
        if int(char) % 2 == 1:  # string --> integer
            list.append(int(char))
    for i in range(len(list)):  # Traverse all the elements in the list and add them together
        sum += list[i]
    print(sum)


if __name__ == "__main__":
    q1_input = float(input("q1: "))
    question_1(q1_input)

    q2_input = float(input("q2: "))
    question_2(q2_input)

    q3_input = int(input("q3= "))

    q4_input_n1 = float(input("q4_n1: "))
    q4_input_n2 = float(input("q4_n2: "))
    q4_input_n3 = float(input("q4_n3: "))
    question_4(q4_input_n1, q4_input_n2, q4_input_n3)

    q5_input_n1 = float(input("q5_n1: "))
    q5_input_n2 = float(input("q5_n2: "))
    q5_input_n3 = float(input("q5_n3: "))
    question_5(q5_input_n1, q5_input_n2, q5_input_n3)

    q6_input_mode = int(input("Please choose the mode:\nStrict --> 0\nLenient --> 1\n"))
    q6_input_n1 = float(input("q6_n1:"))
    q6_input_n2 = float(input("q6_n2:"))
    q6_input_n3 = float(input("q6_n3:"))
    question_6(q6_input_mode, q6_input_n1, q6_input_n2, q6_input_n3)

    q7_input_n1 = int(input("q7_n1: "))
    q7_input_n2 = int(input("q7_n2: "))
    q7_input_n3 = int(input("q7_n3: "))
    question_7(q7_input_n1, q7_input_n2, q7_input_n3)

    q8_input_n1 = int(input("q8_n1: "))
    q8_input_n2 = int(input("q8_n2: "))
    q8_input_n3 = int(input("q8_n3: "))
    q8_input_n4 = int(input("q8_n4: "))
    question_8(q8_input_n1, q8_input_n2, q8_input_n3, q8_input_n4)

    q9_input_scalar = int(input("Please choose the scalar:\nCelsius --> 0\nFahrenheit --> 1\n"))
    q9_input_temp = float(input("Please enter the temperature:"))
    question_9(q9_input_scalar, q9_input_temp)

    q10_input_grade = input("Enter a letter grade: ")
    question_10(q10_input_grade)

    question_11()

    question_12()

    question_13()

    q14_input_a = int(input("Please enter the began number a: "))
    q14_input_b = int(input("Please enter the ending number b: "))
    question_14(q14_input_a, q14_input_b)

    q15_input = int(input("Please input an integer!!: "))
    question_15(q15_input)
