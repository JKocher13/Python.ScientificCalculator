import unittest
from calculator import Calculator

from mainApp import getFirstNumber, getTwoNumbers
class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(-4, 3), -7)

   def test_sub3(self):
        c = Calculator()
        self.assertEqual(c.sub(123.2, .2), 123)
    
   def test_mul1(self):
        c = Calculator()
        self.assertEqual(c.mul(4, .5), 2)

    def test_mul2(self):
        c = Calculator()
        self.assertEqual(c.mul(5, 5), 25)
    
    def test_mul3(self):
        c = Calculator()
        self.assertEqual(c.mul(10, -1), -10)
   
    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 25,5 ), 5)

    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)
    
    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)
 
    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)

    val = "4.0"

    @patch('builtins.input', return_value=val)
    def test_getFirstNumber(self, mock_input):
        result = getFirstNumber();
        self.assertEqual(float(4.0), result)


    val = "4.3"


    @patch('builtins.input', return_value=val)
    def test_getSecondNumber(self, mock_input):
        result = getFirstNumber();
        self.assertEqual(float(4.3), result)


    val = float(4.3)
    val2 = float(3.4)


    @patch('mainApp.getFirstNumber', return_value=val)
    @patch('mainApp.getSecondNumber', return_value=val2)
    def test_getTwoNumbers(self, mock_input, mock_input2):
        result = getTwoNumbers();
        self.assertEqual(result, (float(4.3), float(3.4)))

if __name__ == '__main__':
    unittest.main()
