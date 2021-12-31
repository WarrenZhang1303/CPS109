"""
Peirong Zhang
This is a simple note program for recording daily schedules. It has five main functions:
1. read all notes: it will print out all your daily schedules on the screen.
2.add a new item: This function allows users to add a new item at the end of the note
3.rewrite the specified note: This function allows users to rewrite a specified item in the file.
4.Delete the specified item: This function allows users to delete a specified item in the file.
5. Create a new .txt file at specified path.
*When the user creates a new note file, the date will be automatically added to the first line of the file.
Because I think date can make this note program look more professional.XD
"""
import time  # this module is used to printout the date.
import os  # this module is used to determine whether the path entered by the user is valid and to avoid errors

"""
notes_create() function will only be called when the user creates a new file.
It will create a writable file and print the date of creation on the first line of the file
"""


def notes_create(file_path):
    with open(file_path, "w") as note:
        note.write(time.strftime("%d,%m,%Y\n", time.localtime()))  # DAY,MONTH,YEAR


"""
notes_read() function open the specified file in read-only mode, 
and traverse each line of the file through the headlines() function
In order for the user to see how many lines of content there are, 
there will be the current number of lines before each line of content.
"""


def notes_read(file_path):
    print("******")  # decoration
    with open(file_path, "r") as note:  # r: only read
        note_list = note.readlines()  # readlines() type is a list.
        times = 0
        while times < len(note_list):
            print(times, "--", note_list[times], end="")  # There will be a visible "\n" at the end of each element,
            # and print() method originally has "\n" symbol, so it needs to be removed with end=""
            times += 1
    print("******")


"""
notes_write(): Open the file in a mode that can read ，write and it won't overwrite the original content. (a+)
To ensure that each input of information is exclusive a line, 
it need to add a "\n" symbol at the end of the user input.
"""


def notes_write(file_path, user_input):
    information = user_input + "\n"
    with open(file_path, "a") as note:
        note.write(information)  # The pointer to a+ mode will automatically point to the last line of the file.


"""
notes_rewrite(): First, open the file in a only read mode.
Then,through readlines() method to store the contents of each lines.
After that, remove the elements of the specified location based on the numbers entered by the user.
Then, use .insert() method insert the new information in the same location. 
Finally, open the file in a only write mode. (w)
Override the original content by traversing the new arranged elements in the list.
"""


def notes_rewrite(file_path, line_number, user_input):
    information = user_input + "\n"  # Make sure that the information entered by the user is on a single line
    pointer = True  # Used to determine whether the number of line entered by the user is valid
    with open(file_path, "r") as note:
        note_list = note.readlines()
        if line_number > (len(note_list) - 1):
            print("There have nothing can be change! Please try again!\n")
            pointer = False  # number of line is invalid
        else:
            note_list[line_number]=information
            # del (note_list[line_number])  # delete that line
            # note_list.insert(line_number, information)  # insert new information at same position
    if not pointer:
        pass  # Return to the menu
    else:
        with open(file_path, "w") as note:  # w mode: New content overrides old content
            for i in range(len(note_list)):
                note.write(note_list[i])
        print("Line:", line_number, "has been changed:)")  # mark


"""
notes_delete(): It's basically the same as the note_rewrite(),
except for the insertion information part.
"""


def notes_delete(file_path, line_number):
    pointer = True
    with open(file_path, "r") as note:
        note_list = note.readlines()
        if line_number > (len(note_list) - 1):
            print("There have nothing can be delete! Please try again!\n")
            pointer = False
        else:
            del (note_list[line_number])
    if not pointer:
        pass
    else:
        with open(file_path, "w") as note:
            for i in range(len(note_list)):
                note.write(note_list[i])
        print("Line:", line_number, "has been deleted:)")  # mark


"""
The default path is： /Users/peirongzhang/Desktop/
The user can choose to change the path, and if it is illegal, 
I/O will warning the user and returns to the menu.
user must input a file name. 

"""
if __name__ == "__main__":
    path = '/Users/peirongzhang/Desktop/'

    print("************************************")
    print("Welcome to use Daily Notes program!!")
    print("************************************")
    print("The current path is:", path)
    while True:
        ans = input("Do you want to change the path?: \n--Y --N\n")
        if ans == "Y" or ans == "y":
            path = input("Please enter a new path: ")
            if os.path.exists(path):
                print("Path has changed.")
                break
            else:
                print("Please enter a correct path!")
        elif ans == "N" or ans == "n":
            print("OK")
            break
        else:
            print("Please try again!")
            print("Y=Yes N==no\n")


    while True:
        file_name = input("Please enter the file name. "
                          "\nIf there have no exact file name,it will create a new file： ")
        if len(file_name) == 0:
            print("You must enter a file name!!\n")
        else:
            break
    file_path = path + file_name + ".txt"

    if not os.path.exists(file_path):
        notes_create(file_path)
        print("\nYou have been create a new note.")
    while True:
        notes_mode = input("\nSo,what do you want to do now?:\n1--read all "
                           "notes\n2--add a note\n"
                           "3--rewrite the specified note\n4--delete the specified note\nq--Quite\n")
        if notes_mode == "1":
            notes_read(file_path)
        elif notes_mode == "2":
            user_input = input("Please write your note below:\n")
            notes_write(file_path, user_input)
            print("Done!:)")
        elif notes_mode == "3":
            notes_read(file_path)
            line_number = int(input("Which line do you want to rewrite? "
                                    "Please input the line number: "))
            user_input = input("Please write your new note below:\n")
            notes_rewrite(file_path, line_number, user_input)
        elif notes_mode == "4":
            notes_read(file_path)
            line_number = int(input("Which line do you want to delete?"
                                    "Please input the line number: "))
            notes_delete(file_path, line_number)
        elif notes_mode == "q":
            print("Thanks for using. Goodbye! OuO")
            break
        else:
            print("HAVE NO SUCH MODE! PLEASE TRY AGAIN!\n")
