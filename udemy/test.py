def counter(a,range):
    while a<=range:
        collection=[]
        a+=1
        collection.append(a)
        return collection

import unittest
class Tests(unittest.TestCase):

    def setUp(self):
        self.name='John'

    def test_case1(self):
        self.assertEqual(counter(0,15), [1])


number=5
while number<=15:
        collection=[]
        number+=1
        collection.append(number)
        print(collection)
