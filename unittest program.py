import unittest

def add(a,b):
    return a+b
class test(unittest.TestCase):
    def test(self):
        self.assertEqual(add(10,20),30)

if __name__ == "__main__":
    unittest.main()        