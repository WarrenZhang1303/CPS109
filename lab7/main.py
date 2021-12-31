import random

"""
A run is a sequence of adjacent repeated values. 
Write a program that generates a sequence of 20 random die tosses and then prints the die values,
 marking the runs by including them in parentheses,
"""


def q1():
    values = []
    for i in range(0, 20):
        values.append(random.randint(1, 6))  # random numbers from 1 to 6
    print(values)  # show the random list
    inRun = False

    for i in range(len(values)):
        if inRun:  # True: find the tail adjacent repeated values
            if values[i] != values[i - 1]:
                # what if there have two constant adjacent repeated values?
                if i != len(values) - 1 and values[i] == values[i + 1]:
                    print(")(", end="")
                    inRun = True
                else:
                    print(")", end="")
                    inRun = False
        else:  # False: find the head of adjacent repeated values
            if i != len(values) - 1 and values[i] == values[i + 1]:  # element not the last one, and is same as next
                # one.
                print("(", end="")
                inRun = True
        print(values[i], end="")  # not a adjacent repeated value

    if inRun:  # True: the last element also is a adjacent repeated value
        print(")")
    else:
        print("")


"""
Write a program that generates a sequence of 20 random die tosses 
and that prints the die values, marking only the longest run
"""


def q2():
    ram = []  # store each adjacent repeated values position
    values = []  # store random numbers from 1~6
    number = []  # store length of each adjacent repeated values
    for i in range(0, 20):
        values.append(random.randint(1, 6))
    print(values)  # show the random list
    inRun = False

    for i in range(len(values)):
        if inRun:  # True: find the tail adjacent repeated values
            if values[i] != values[i - 1]:
                # what if there have two constant adjacent repeated values?
                if i != len(values) - 1 and values[i] == values[i + 1]:
                    y = i - 1  # tail position
                    ram.append((x, y))  # have fond the adjacent repeated values
                    x = i  # head position
                else:
                    y = i - 1  # tail position
                    ram.append((x, y))  # have fond the adjacent repeated values
                    inRun = False
        else:  # False: find the head of adjacent repeated values
            if i != len(values) - 1 and values[i] == values[i + 1]:
                x = i  # head position
                inRun = True
    if inRun:
        y = len(values) - 1  # if  the last element in the list is tail
        ram.append((x, y))
        """
        YOU HAVE FOUND ALL ADJACENT REPEATED VALUES 
        THEIR POSITIONS ARE IN THE ram LIST
        """
    # what if there have no adjacent repeated values
    if len(ram) == 0:
        return [print(a, end="") for a in values]

    # calculate their length
    for i in range(len(ram)):
        number.append(ram[i][1] - ram[i][0])
    # Find the max length value
    max_value = max(number)
    """
    Marking all runs by including them in parentheses
    """
    for i in range(len(ram)):
        # insert with reverse order  won't mess up the order
        if ram[len(ram) - 1 - i][1] - ram[len(ram) - 1 - i][0] == max_value:
            values.insert(ram[len(ram) - 1 - i][1] + 1, ")")  # from right-->left
            values.insert(ram[len(ram) - 1 - i][0], "(")
    [print(a, end="") for a in values]  # list comprehension
    print("\n")


"""
. Assume that L is a list of Boolean values, True and False. 
Write a function longestFalse(L) which returns a tuple (start, end) representing the start and end 
indices of the longest run of False values in L. If there is a tie, then return the first such run.
"""


def longestFalse(L):
    pointer = False
    ram = []  # store each adjacent False values position
    number = []  # store length of each adjacent False values
    ans = []  # store all longest values in the list
    for i in range(len(L)):
        if not L[i]:  # value==False
            if not pointer:  # And it is the head
                x = i  # head position
                pointer = True  # Now, go find the tail
        else:  # value==True
            if pointer:  # And you need a tail
                y = i - 1  # tail position
                ram.append((x, y))
                pointer = False  # Now, go find a new head

    if pointer:  # what if the tail is the last element
        y = len(L) - 1
        ram.append((x, y))
        """
           NOW, FIND THE LONGEST LENGTH
        """
    # ALL TRUE?!!
    if len(ram) == 0:
        return None
    # calculate their length
    for i in range(len(ram)):
        number.append(ram[i][1] - ram[i][0])
    # Find the biggest values
    biggest = max(number)

    for i in range(len(ram)):  # insert with reverse order  won't mess up the order
        if ram[len(ram) - 1 - i][1] - ram[len(ram) - 1 - i][0] == biggest:
            ans.append(ram[len(ram) - 1 - i])
    # return all allow tuples in a list
    return ans


"""
Write a function occupy(n), which shows how birds are going to occupy n nests,
 assuming that each new bird will choose the nest in the middle of the largest unoccupied run of nests. 
 You could use as a helper method longestFalse(L) from the previous question. 
"""


def occupy(n):
    # Assume the default value is False
    sample = [False for i in range(0, n)]  # list comprehension
    """
    Target->Turn all False--> True
    """
    L = longestFalse(sample)  # I m a list :)
    while L is not None:  # While not all true
        [print("_", end="") if sample[i] == False else print("X", end="") for i in range(0, n)]
        print("")  # Change the line
        for i in range(len(L)):
            # Turn the longest  adjacent False values 's middle False-->True
            x = (L[i][0] + L[i][1]) // 2
            sample[x] = True
        L = longestFalse(sample)  # repeat
    [print("_", end="") if sample[i] == False else print("X", end="") for i in range(0, n)]  # print the last line
    print("")


"""
 Write a function isPal(L), where L is a list of integers, 
 and the function returns True if the list is a palindrome, 
 False otherwise. For example [5, 2, 9, 9, 2 5] is a palindrome. 
 Use the reverse() method of list and check if the reversed list is the same as the original list.
"""


def isPal(L):
    # EMPTY LIST
    if len(L) == 0:
        print("Empty list")
        return True
    for i in range(0, len(L) // 2):  # middle position in the list
        if L[i] != L[len(L) - 1 - i]:  # left: 0-->middle  right: last position-->middle
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    Q1
    """
    print("Q1")
    q1()
    """
    Q2
    """
    print("Q2")
    q2()
    """
    Q3
    """
    print("Q3")
    M = []
    for i in range(0, 20):
        x = random.randint(0, 1)
        if x == 1:
            M.append(True)
        else:
            M.append(False)
    print(M)
    print(longestFalse(M))
    """
    Q4
    """
    print("Q4")
    occupy(10)
    """
    Q5
    """
    print("Q5")
    Paw = [5, 2, 9, 7, 9, 2, 5]
    print(Paw)
    print(isPal(Paw))

    dirty_Paw = Paw
    dirty_Paw.reverse()
    print("Use the reverse() method: ", Paw == dirty_Paw)
"""
OUTPUT
Q1
[3, 2, 1, 6, 3, 1, 4, 1, 2, 2, 2, 4, 6, 3, 2, 2, 4, 5, 4, 6]
32163141(222)463(22)4546
Q2
[3, 3, 6, 6, 3, 3, 4, 5, 2, 1, 3, 5, 3, 1, 1, 1, 2, 3, 4, 6]
3366334521353(111)2346

Q3
[False, False, False, False, True, True, False, True, True, False, True, False, False, False, False, False, True, True, False, True]
[(11, 15)]
Q4
__________
____X_____
____X__X__
_X__X__X__
_XX_XX_XX_
XXXXXXXXXX
Q5
[5, 2, 9, 7, 9, 2, 5]
True
Use the reverse() method:  True
"""
