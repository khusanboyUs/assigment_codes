#FUNCTIONS
import unittest


def sample_case1(a,b):
    return a+b

def sample_case2():
    return 10+2

class TestCases(unittest.TestCase):
    def test1(self):
        self.assertEqual(sample_case1(5,5),10)

    def test2(self):
        self.assertEqual(sample_case2(),12)



