import pytest

class Calculator:
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

Calculator = Calculator()

def test_subtract():
    assert Calculator.subtract(10,2) == 8  #case a > b (positive result)
    assert Calculator.subtract(2,10) == -8  #case a < b (negative result)
    assert Calculator.subtract(10, -2) == 12  #case a > 0 and b < 0 (positive result) 
    assert Calculator.subtract(-2, 10) == -12 #case a < 0 and b < 0 (negatice result)
    assert Calculator.subtract(1.5,1.5) == 0 #case a = b and both are float
    assert Calculator.subtract(0,0) == 0 #case a = b = 0

def test_multiply():
    assert Calculator.multiply(1,2) == 2
    assert Calculator.multiply(1.5,1.5) == 2.25
    assert Calculator.multiply(0,1000) == 0
    assert Calculator.multiply(100000000000000, 1) == 100000000000000

    
