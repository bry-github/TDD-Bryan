import pytest

def divide(a, b):
    return a / b

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        print("Trying to divide by 0")
        divide(5,0)

#print(divide(5,0))
