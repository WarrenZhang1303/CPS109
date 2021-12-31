from a2_main import a2
import unittest
import os


class Task06_test(unittest.TestCase):

    def setUp(self):
        a2.frequency_word("unique_QA_Pairs.txt")

    def test01(self):
        self.assertTrue(os.path.isfile("Frequency.txt"))

    # what if it give an empty file?
    def test02(self):
        self.assertTrue(a2.frequency_word("t1_empty.txt") == {})


if __name__ == "__main__":
    unittest.main(exit=True)
