from a2_main import a2
import unittest


class Tesk01_test(unittest.TestCase):
    """
    If you want to run the whole test, you need a "QA_Pairs.txt"
    """
    # 1.the length of pair should be an even number and it is the half length of total length
    def test1(self):
        with open("QA_Pairs.txt", "r") as test_file:
            l = len(test_file.readlines())
        self.assertEqual(len(a2.QA_pairs("QA_Pairs.txt")), l // 2)

    # 2. what if the total lines is an odd number.
    def test2(self):
        with open("t1_test.txt", "r") as test2_file:
            L = len(test2_file.readlines())
        self.assertEqual(len(a2.QA_pairs("t1_test.txt")), L // 2)

    # 3. what if it give an empty file?
    def test3(self):
        self.assertEqual(len(a2.QA_pairs("t1_empty.txt")), 0)


if __name__ == "__main__":
    unittest.main(exit=True)
