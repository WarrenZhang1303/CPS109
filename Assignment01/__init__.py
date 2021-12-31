import time
import os


def notes_create(file_path):
    with open(file_path, "a+") as note:
        note.write(time.strftime("%d,%m,%Y\n", time.localtime()))


def notes_read(file_path):
    with open(file_path, "r") as note:
        note_list = note.readlines()
        times = 0
        while times < len(note_list):
            print(times, "--", note_list[times], end="")
            times += 1


def notes_write(file_path):
    with open(file_path, "a") as note:
        for i in range(5):
            note.write("Hell\n")


def notes_delete(file_path, line_number):
    pointer = True
    notes_read(file_path)
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
        print("Line:", line_number, "has been deleted:)")


def note_rewrite(file_path, line_number, user_input):
    pointer = True
    with open(file_path, "r") as note:
        note_list = note.readlines()
        if line_number > (len(note_list) - 1):
            print("There have nothing can be change! Please try again!\n")
            pointer = False
        else:
            del (note_list[line_number])
            note_list.insert(line_number, str(user_input))
    if not pointer:
        pass
    else:
        with open(file_path, "w") as note:
            for i in range(len(note_list)):
                note.write(note_list[i])
        print("Line:", line_number, "has been changed:)")


if __name__ == "__main__":
    path = '/Users/peirongzhang/Desktop/'
    file_name = "testfiles"
    file_path = path + file_name + ".txt"
    # notes_create(file_path)
    notes_write(file_path)
    # notes_delete(file_path, 7)
    notes_read(file_path)
    note_rewrite(file_path,3,"hello")
