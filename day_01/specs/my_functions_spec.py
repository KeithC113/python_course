import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from my_functions import * 

class FunctionsPracticeTest(unittest.TestCase):
    def test_greet(self):
        #ARRANGE 
        #ACT
        greeting = greet("Keith", "Afternoon")

        #ASSERT
        self.assertEqual(greeting, "Good Afternoon, Keith!")

    def test_greet_capitalises_name(self):
        greeting = greet ("theodore", "morning")
        self.assertEqual(greeting, "Good morning, Theodore!")

    def test_add(self):
        result = add(2,3)
        self.assertEqual(5,result)


if __name__ == "__main__":
    unittest.main()