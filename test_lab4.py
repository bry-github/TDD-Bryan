import pytest

class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a + b


@pytest.fixture
#calc = Calculator("Calc 1")
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)

    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)

    assert True
    
def test_lab4_test2(base_calculator):
    print("#2 this calculator's name is " + base_calculator.name)

    #calc.name = "Calc 2"
    #print("This calculator's name is " + calc.name)

    #print(calc.add(1,1))
    assert True
