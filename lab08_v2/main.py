"""
Q1
Write a recursive function to add a positive integer b to another number a, add(a, b),
where only the unit 1 can be added, For example add(5, 9) will return 14.
The pseudocode is:
# Base case: if b is 1, you can just return a + 1
# General case: otherwise, return the sum of 1 and what is returned by adding a and b - 1.
"""


def add(a, b):
    # Base case: if b is 1, you can just return a + 1
    if b == 0:  # Exit is here
        return a
    else:
        # General case: otherwise, return the sum of 1 and what is returned by adding a and b - 1.
        a = a + 1
        b = b - 1
        return add(a, b)


"""
Q2
Write a function log2(x), 
which gives an integer approximation of the log base 2 of a positive number x, 
but it does so using recursion. 
Use a base case where you return 0 if x is 1 or less. 
In the general case, add 1 to the answer and divide x by 2. 
"""


def log2(x):
    # base case: return 0 if x is 1 or less
    if x <= 1:
        return 0
    else:
        # general case: add 1 to the answer and divide x by 2.
        return 1 + log2(x // 2)


"""
Q3
Write a recursive function reverse(sentence) for reversing a sentence. 
For example, reverse('Who let the dogs out?') will return '?tuo sgod eht tel ohW'. 
The idea is to remove the first or last letter, reverse the shortened sentence, 
and then combine the two parts.
"""


def reverse(setence):
    # Base case: all letters have moved out.
    if setence == "":
        return ""
    else:
        # remove the last letter, reverse the shortened sentence, and then combine the two parts
        return setence[len(setence) - 1] + reverse(setence[:len(setence) - 1])


"""
04 & Q5
Write a recursive function power(x, n), 
where n is 0 or a postive integer. 
For example, power(2, 10) will return 1024. 
Write a suitable base case, 
and for the general case use the idea that xn = x * x**(n-1).

Define a global variable, countcalls, 
and increment it inside the power(x, n) function that you wrote for Q4, 
so that it counts the number of times the power function is called. 
Show that it produces the expected number of calls for power(2, 10) and 
power(5, 10) and power(5, 0), each separately..
"""


def power(x, n, ):
    global countcalls
    countcalls += 1
    # Base case: return 1 if n==0 x^0=1 or return 0 if x==0

    if x == 0:
        print("countcall(01): ", countcalls)
        return 0
    elif n == 0:
        print("countcall(01): ", countcalls)
        return 1
    else:
        # General case: x**n=x*(x**(n-1))
        return x * power(x, n - 1)


"""
Q6 
Improve on your function from Q4, 
calling it powerHalf(x, n), 
where this function is recursive like power(x, n), 
but it also uses the idea that xn = (xn/2)2 when n is even. 
Use the countcalls variable (as in Q5) to verify that this version of the power function is more efficient.
"""


def powerHalf(x, n):
    global countcalls
    countcalls += 1
    # Base case: return 1 if n==0 x^0=1 or return 0 if x==0
    if x == 0:
        print("countcall(02):", countcalls)
        return 0
    elif n == 0:
        print("countcall(02):", countcalls)
        return 1
    else:
        # General case: when n is even x**n=(x**(n/2))**2
        if n % 2 != 0:
            return x * power(x, n - 1)
        else:
            return powerHalf(x, n / 2) ** 2


"""
Q7
Attached to this lab is a file representing a DNA sequence. 
The first line starts with '>' and is a comment, 
and the lines after that hold the sequence. 
The sequence has letters 'A', 'C', 'T', and 'G'. In your program for this question, 
read the sequence using the statements.

Also write a function gcContent(sequence), 
which returns the percent of the sequence which is either 'G' or 'C'. 
Use your function on the input sequence and print the results.
"""


def q7():
    # -----------------------------------------------------q7 # Reading from a file
    # -----------------------------------------------------
    f = open('kdpF.txt')  # opens a file for reading
    line = f.readline()  # reads a single line
    print(line)
    seq = ''
    for line in f:  # reading the rest of the lines
        seq = seq + line
    seq = seq.replace('\n', '')  # removing the newline characters
    seq = seq.upper()
    print(seq)
    """
    There only have 199 bp region of the chromosomes in kdpF.txt
    """
    total = len(seq)

    def gcContent(sequence):  # You do the rest
        """
        :base case: return 0 when all letter pop out.
        :general case: if the first letter is "C" OR "G" ,ans+=1,then pop it out. Or,return 0 then pop it out.
        """
        if sequence == "":
            return 0
        else:
            if sequence[0] == "C" or sequence[0] == "G":
                return 1 + gcContent(sequence[1:])
            else:
                return 0 + gcContent(sequence[1:])
        pass

    return gcContent(seq) / total * 100


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Q1
    print("# Q1")
    print("3+17=", add(3, 17))

    # Q2
    print("\n# Q2")
    print("log2(128)=", log2(128))

    # Q3
    print("\n# Q3")
    print("Who let the dogs out?-->", reverse('Who let the dogs out?'))

    # 04 & Q5
    print("\n# 04 & Q5")
    countcalls = 0
    print("power(2, 8): ", power(2, 8))

    # 06
    print("\n#06")
    countcalls = 0
    print("powerHalf(2,8):", powerHalf(2, 8))

    # 07
    print("\n#07")
    print("There actually only have 199 bp region of the chromosome in kdpF.txt")
    print(" the percent of the sequence which is either 'G' or 'C': ", q7(), "%")
