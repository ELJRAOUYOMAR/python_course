import unittest

class MyTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(10 > 2, "must be True")

    def test_two(self):
        self.assertEqual(20 + 2, 22, "must be equal")

    def test_three(self):    
        self.assertEqual(20 + 3, 23, "must be equal")

class MyTest2(unittest.TestCase):
    def test_one(self):
        self.assertTrue(10 > 2, "must be True")

    def test_two(self):
        self.assertEqual(20 + 2, 22, "must be equal")

    def test_three(self):    
        self.assertEqual(20 + 3, 23, "must be equal")



if __name__ == "__main__":
    unittest.main()
