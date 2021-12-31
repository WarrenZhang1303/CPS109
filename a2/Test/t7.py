from a2_main import a2
import unittest
import os


class Task07_test(unittest.TestCase):
    def setUp(self):
        x = a2.frequency_word("unique_QA_Pairs.txt")
        self.target = a2.sort_frequency(x)
        self.test = list(self.target.values())
        self.y = sorted(self.test, reverse=True)

    #
    def test01(self):
        self.assertTrue(os.path.isfile("Decreasing_Frequency.txt"))

    # Check if the words is  decreasing order
    def test02(self):
        self.assertEqual(self.test, self.y)


if __name__ == "__main__":
    unittest.main(exit=True)
