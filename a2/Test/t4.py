from a2_main import a2
import unittest
import os.path


class Task04_test(unittest.TestCase):
    def setUp(self):
        f = "unique_QA_Pairs.txt"
        x = a2.turn_to_dictionary(f)
        a2.questions(x)
        with open("Questions.txt") as question:
            self.test = len(question.readlines())
        with open("unique_QA_Pairs.txt") as unique:
            self.sample = len(unique.readlines())

    # Should have a "Questions.txt" file
    def test01(self):
        self.assertTrue(os.path.isfile("Questions.txt"))

    # the number of lines in "Questions.txt should be half of total"
    def test02(self):
        self.assertEqual(self.test, self.sample / 2)


if __name__ == "__main__":
    unittest.main(exit=True)
