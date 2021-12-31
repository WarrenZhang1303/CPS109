# Find the fourth root of a integer
def q1():
    x = int(input("Enter an integer: "))
    ans = 0
    while ans ** 4 < abs(x) and x != 0:  # To prevent an error when input==0
        ans += 1
    if ans ** 4 != abs(x) or x < 0:  # negative number  have no perfect forth root
        print(x, " has not a prefect forth root.")
    else:
        print("Forth root of ", x, " is ", ans)


# Find the integer 's root and lowest power
def q2():
    x = int(input("Q2: Enter an integer: "))
    power = 2  # the range of power are 1< power  <6
    while power <= 6:  # power ==6 is for some special situations. For example x=-9
        ans = 0
        while ans ** power < abs(x) and x != 0:  # To prevent an error when input==0
            ans += 1

        if power == 6:  # out of range ,or no result
            print("NO integer or real roots")
            break

        elif ans ** power == abs(x):
            if x < 0 and power % 2 == 0:  # special situation when power is an even number
                power += 1  # negative number  have no real even power and real roots
            else:
                if x < 0:
                    ans = -ans
                print("(", ans, ") **", power, " is equal to the ", x)
                break

        else:
            power += 1


# Find the integer 's root and the largest power
def q3():
    x = int(input("Q3: Enter an integer: "))
    power = 5  # the range of power are 1< power  <6
    while power >= 1:  # reverse order loop (5-4-3-2)
        ans = 0
        while ans ** power < abs(x) and x != 0:  # To prevent an error when input==0
            ans += 1

        if power == 1:  # out of range ,or no result
            print("NO integer or real roots")
            break

        elif ans ** power == abs(x):
            if x < 0 and power % 2 == 0:  # special situation when power is an even number
                power -= 1  # negative number  have no real even power and real roots
            else:
                if x < 0:
                    ans = -ans
                print("(", ans, ") **", power, " is equal to the ", x)
                break

        else:
            power -= 1


# Print the phrase N times
def q4():
    N = int(input("Please input an integer: "))
    phrase = input("Please enter a phrase: ")
    for i in range(N):  # i=0, for i<N
        print(phrase)


# Print the largest odd number
def q5():
    t = 0  # default value
    room = []  # list "room" is used to store user's input
    while t < 10:
        x = int(input("Please input an integer:"))
        if x % 2 == 1:  # only the odd number can be stored in the list
            room.append(x)
        t += 1

    if len(room) != 0:  # len==0 means there have no odd number
        ans = room[len(room) - 1]  # the last elements in the list
        for i in range(len(room)):  # exhaustive the list
            if room[i] >= ans:  # find the largest number
                ans = room[i]
        print("The largest odd number is: ", ans)
    else:

        print("There have no largest odd number!")


# Print the sum of the digits in the string
def q6():
    library = "0123456789"  # Stored all possibility
    ans = 0  # default value
    user_input = input("Please enter a string: ")
    for char in user_input:
        if char in library:  # only record the char which appeared in the 'library'
            ans += int(char)  # String-->integer
    print(ans)


# Read a string from the user which
# is a sequence of decimal numbers separated by commas.
def q7():
    user_input = input("Please enter a string: ")
    room = user_input.split(",")  # Separate string with ","
    # , the type of room is a list.
    ans = 0  # default values
    for i in range(len(room)):
        ans += float(room[i])
    print("%.3f" % ans)  # Accurate to three decimal places


# Bisection search to find the square root of positive number x.
def q8():
    while True:
        x = float(input("Please enter a positive number: "))
        if x > 0:
            break  # only if the user input the positive number can break this loop

    epsilon = 0.01  # error value
    low = 0.0
    high = max(1.0, x)  # high==1 when input<1
    ans = (high + low) / 2.0
    while abs(ans ** 2 - x) >= epsilon:
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print(ans, "is close to square root of ", x)


# Uses bisection search to find the cube root of a number,
def q9():
    x = float(input("Please enter a number: "))

    epsilon = 0.01  # error value
    low = 0.0
    high = max(1.0, abs(x))  # high==1 when input<1.
    # abs(x) Assume the input is positive.
    ans = (high + low) / 2.0
    while abs(ans ** 3 - abs(x)) >= epsilon:
        if ans ** 3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0

    if x < 0:  # if the input is negative the cube root also is negative
        ans = -ans
    print(ans, "is close to cube root of ", x)


#   convert a positive decimal integer to binary
def q10():
    room = []  # used to store binary result (original order)
    while True:  # only if the user input the positive integer can break this loop
        n = int(input("Please enter a positive integer: "))
        if n > 0:
            break

    print(n, "to binary--> ", end="")  # "end=" used to print out the string without line break
    while n != 0:
        room.append(n % 2)  # store the modulus result to the "room" list
        n = n // 2  # keep the divided result to the next round
    for i in range(len(room)):
        print(room[len(room) - i - 1], end='')  # print out elements from "room" list
        # (with reverse order)
        i += 1
    # print("\n", room)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()

