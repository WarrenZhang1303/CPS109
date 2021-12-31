from a2_main import a2
import unittest
import os.path


class Task03_test(unittest.TestCase):
    def setUp(self):
        f = "unique_QA_Pairs.txt"
        a2.turn_to_dictionary(f)
        self.target = a2.turn_to_dictionary(f)

    # Should have create one files.
    def test1(self):
        self.assertTrue(os.path.isfile("QA dictionary"))

    # The type should be dictionary
    def test2(self):
        self.assertTrue(type(self.target) == dict)


if __name__ == "__main__":
    unittest.main(exit=True)
