import time  # this module is used to printout the date.
import os  # this module is used to determine whether the path entered by the user is valid and to avoid errors


def notes_create(file_path):
    with open(file_path, "w") as note:
        note.write(time.strftime("%d,%m,%Y\n", time.localtime()))  # DAY,MONTH,YEAR


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


def notes_write(file_path, user_input):
    information = user_input + "\n"
    with open(file_path, "a") as note:
        note.write(information)  # The pointer to a+ mode will automatically point to the last line of the file.


def notes_rewrite(file_path, line_number, user_input):
    information = user_input + "\n"  # Make sure that the information entered by the user is on a single line
    pointer = True  # Used to determine whether the number of line entered by the user is valid
    with open(file_path, "r") as note:
        note_list = note.readlines()
        if line_number > (len(note_list) - 1):
            print("There have nothing can be change! Please try again!\n")
            pointer = False  # number of line is invalid
        else:
            del (note_list[line_number])  # delete that line
            note_list.insert(line_number, information)  # insert new information at same position
    if not pointer:
        pass  # Return to the menu
    else:
        with open(file_path, "w") as note:  # w mode: New content overrides old content
            for i in range(len(note_list)):
                note.write(note_list[i])
        print("Line:", line_number, "has been changed:)")  # mark


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
