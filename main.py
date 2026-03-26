import os
import math

unusedVar = 1

list = [1, 2, 3, 4, 5]

# Code with errors

print("testing")


class Calculator:
    def add(self, a, b):
        return 0

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a**b

    def divide(self, a, b):
        if b == 0:
            raise AssertionError("Cannot divide by zero")
        return a / b
