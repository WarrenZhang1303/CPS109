"""
Task 01
How many QA pairs in QA_Pairs.txt?
"""


def QA_pairs(file_name):
    """
    :param file_name: target file
    :return:A list with ["Q","A"] format
    """
    with open(file_name, encoding="UTF-8-sig") as copy:
        file_list = copy.read().splitlines()

        pairs = []  # Used to  store Questions and Answers
        # even elements in list are Answers
        for i in range(len(file_list)):
            if i % 2 == 0:
                y = file_list[i]
                # Odd elements in list are Questions
            else:
                x = file_list[i]
                pairs.append([x, y])
    return pairs


"""
Task 02
"""


def unique_pairs(file_name):
    """
    Create two .txt files, which names are "unique_QA_Pairs" and
    "Overlapping.txt" with write model.
    """
    # implement Task 01 function, which is a list store pairs of Q and A
    ram = QA_pairs(file_name)
    with open("unique_QA_Pairs.txt", "w") as unique:
        with open("Overlapping.txt", "w") as overlapping:

            while ram:
                pointer = []  # Stores the overlap pairs index
                for i in range(1, len(ram)):  # Set ram[0] as the Q1,A1
                    if ram[0] == ram[i]:  # Two same pairs
                        pointer.append(i)
                    elif ram[0][0] == ram[i][0]:  # Have same Question
                        pointer.append(i)
                    elif ram[0][1] == ram[i][1]:  # Have same answer
                        pointer.append(i)
                pointer.reverse()  # overlap pairs index: Last one--> First one
                # It won't mess up the position of elements within the list.

                if pointer:  # Exist overlap pairs
                    #   Depending on the index, write the overlap pairs.
                    for i in range(len(pointer)):
                        x = pointer[i]
                        overlapping.write(ram[x][0] + "\n")
                        overlapping.write(ram[x][1] + "\n")
                        ram.pop(x)  # After done , throw them in the trash.
                #  If there have no overlap pairs or
                #  All overlap pairs compare with ram[0] have been split.
                #  Put first element in the list to the "unique" file.
                unique.write(ram[0][0] + "\n")
                unique.write(ram[0][1] + "\n")
                ram.pop(0)  # After done , throw it in the trash.


"""
Task 03
"""


def turn_to_dictionary(file_path):
    """
    Store the pairs from unique_QA_Pairs.txt as a dictionary.
    :param file_path: unique_QA_Pairs.txt
    :return:Dictionary of unique_QA_Pairs
    """
    d = {}  # Key: answer  Value: Question
    pointer = False
    with open(file_path, "r") as unique_dict:

        ram = unique_dict.read().splitlines()  # A list which store all unique questions answers
        for i in range(len(ram)):
            if pointer:  # True
                d[ram[i]] = x
                pointer = False
            else:  # False
                x = ram[i]
                pointer = True

    # Create files
    def QA_dictionary_file(d):
        """
        Put the dectionary in a file named "QA dictionary"
        :param d: Dictionary type with unique QA pairs
        """
        with open("QA dictionary", "w") as f:
            f.write(str(d))

    QA_dictionary_file(d)
    return d


"""
Task 04
"""


def questions(dict):
    """
    Extract all questions in a file called Questions.txt.
    :param dict: Dictionary from Task 03 unique_QA_Pairs
    :return: None
    """
    with open("Questions.txt", "w") as question:
        values = list(dict.values())
        for i in range(len(values)):
            question.write(values[i] + "\n")


"""
Task 05
"""


def answers(d):
    """
    Extract all answers in a file called Answers.txt.
    :param d: Dictionary from Task 03 unique_QA_Pairs
    :return: None
    """
    with open("Answers.txt", "w") as all_answers:
        keys = list(d.keys())
        for i in range(len(keys)):
            all_answers.write(keys[i] + "\n")


"""
Task 06
"""


def frequency_word(file_path):
    """
    Find the term frequency of each word (that is, the count of each word) in unique_QA_Pairs.txt,
    and output the frequencies as Frequency.txt.
    :param file_path:unique_QA_Pairs.txt
    :return: A dictionary type of Frequency.txt
    """

    """
    Step 01: Pick all words in a list
    """

    def pick_words():
        with open(file_path) as pairs_unique:
            lines = pairs_unique.read().splitlines()  # A list: store each lines information
            sample = " ".join(lines).lower()  # Merge all elements, but split them with a "space",(type:string)
            # also turn them with lower case.

        pointer = False  # Default boolean
        rule = "abcdefghijklmnopqrstuvwxyz"  # Definition of words
        words = []  # Stores evey words from file

        for i in range(len(sample)):
            if pointer:  # Find the tail
                if rule.find(sample[i]) == -1:
                    y = i
                    words.append(sample[x:y])  # HAVE FIND A WORD, put it in the list.
                    pointer = False  # Replete
            else:  # Find the head
                if rule.find(sample[i]) != -1:
                    x = i
                    pointer = True
        # What if the last string not a symbol
        if pointer:
            words.append(sample[x:])
        return words

    """
    Step02: Find the term frequency of each word
    """

    def counting(words):
        ans = {}  # key: world, value: frequency number

        for i in range(len(words)):

            if not ans.get(words[i]):  # If that word is first time appear in the dictionary
                ans[words[i]] = 1  # Create a new key with value 1
            else:  # value+=1
                ans[words[i]] = ans[words[i]] + 1
        return ans

    """
    Step 03: Write the answers in the Frequency.txt
    """

    def storage(dict):
        with open("Frequency.txt", "w") as frequency:
            for key, value in dict.items():
                frequency.write(key + ", " + str(value) + "\n")

    p = pick_words()
    count = counting(p)
    storage(count)
    return count


def sort_frequency(d):
    """
    Rank the words by the decreasing order of their frequencies and output them as Decreasing_Frequency.txt.
    :param d: a dictionary which about the term frequency of each word
    :return:Sorted dictionary
    """
    ram = []  # Used to turn the dictionary to list type
    ans = {}
    for key, value in d.items():
        ram.append((value, key))  # Each elements in the list is a tuple,
        # and the first element in each tuple is the frequency number
    ram.sort(reverse=True)  # sort the list with first element in the tuple.

    with open("Decreasing_Frequency.txt", "w") as f:
        for i in range(len(ram)):
            f.write(ram[i][1] + "," + str(ram[i][0]) + "\n")
            ans[ram[i][1]] = ram[i][0]
    return ans


if __name__ == "__main__":
    file_name = "QA_Pairs.txt"
    file_path = "unique_QA_Pairs.txt"

    # Task 01
    print("There are:", len(QA_pairs(file_name)), "pairs")

    # # Task 02
    unique_pairs("QA_Pairs.txt")
    #
    # # Task 03 & 04
    dict = turn_to_dictionary(file_path)
    questions(dict)
    #
    # # Task 05
    answers(dict)
    #
    # # Task 06&07
    sort_frequency(frequency_word(file_path))
