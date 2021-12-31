from a2_main import a2
import unittest
import os


class Task02_test(unittest.TestCase):
    def setUp(self):
        f = "QA_Pairs.txt"
        f1 = "unique_QA_Pairs.txt"
        f2 = "Overlapping.txt"
        a2.unique_pairs(f)
        with open(f) as test_file:
            self.l = len(test_file.readlines())

        with open(f1) as unique:
            self.u_l = len(unique.readlines())

        with open(f2) as overlap:
            self.o_l = len(overlap.readlines())

    # Should have create two files.
    def test1(self):
        self.assertTrue(os.path.isfile("unique_QA_Pairs.txt") and os.path.isfile("Overlapping.txt"))

    # unique+overlap = total file's length
    def test2(self):
        self.assertEqual(self.u_l + self.o_l, self.l)


if __name__ == "__main__":
    unittest.main(exit=True)
