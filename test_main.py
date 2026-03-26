from main import Calculator
import pytest

calculatorTest = Calculator()


def test_add():
    assert calculatorTest.add(2, 2) == 4
    assert calculatorTest.add(10, 0) == 10
    assert calculatorTest.add(99, 1) == 100


def test_subtract():
    assert calculatorTest.subtract(4, 2) == 2
    assert calculatorTest.subtract(10, 5) == 5
    assert calculatorTest.subtract(1, 5) == -4


def test_multiply():
    assert calculatorTest.multiply(2, 2) == 4
    assert calculatorTest.multiply(10, 5) == 50
    assert calculatorTest.multiply(99, 0) == 0


def test_divide():
    assert calculatorTest.divide(4, 2) == 2
    assert calculatorTest.divide(10, 5) == 2
    assert calculatorTest.divide(1, 5) == 0.2
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculatorTest.divide(10, 0)
