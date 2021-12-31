from a2_main import a2
import unittest
import os


class Task06_test(unittest.TestCase):
    def setUp(self):
        f = "unique_QA_Pairs.txt"
        x = a2.turn_to_dictionary(f)
        a2.answers(x)
        with open("Answers.txt") as ans:
            self.a = len(ans.readlines())
        with open("Questions.txt") as questions:
            self.q = len(questions.readlines())
        with open("unique_QA_Pairs.txt") as unique:
            self.sam = len(unique.readlines())

    # the number of lines in "Questions.txt should be half of total"
    def test01(self):
        self.assertEqual(self.a, self.sam / 2)

    def test02(self):
        self.assertEqual(self.q + self.a, self.sam)

    # Should have "Answers.txt" file
    def test03(self):
        self.assertTrue(os.path.isfile("Answers.txt"))


if __name__ == "__main__":
    unittest.main(exit=True)
