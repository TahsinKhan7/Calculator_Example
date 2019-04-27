#Write our amazing TDD tests here
# Your calculator should
    # Multiply, divide, add, subtract
    # Keep result in the calculator object

# Random lists of tests
# Test for the data type
# Test for addition              # for int/correct operation/output
# Test for subtraction
# Test for multiplication
# Test for division
# Test for last result was recorded

from calculator_sim import *

#Tests have 2 minimum sections
    #setup
    #Assertion

calculator_instance = Calculator()

# Test for addition
print('Test for addition:')
calculator_instance.add(10,10) == 20
calculator_instance.add(100,1) == 101
print(type(calculator_instance.add(1,1)) == int)

# Test for Subtraction
print('Test for subtraction:')
calculator_instance.subtract(10,10) == 0
calculator_instance.subtract(100,1) == 99
print(type(calculator_instance.subtract(1,1)) == int)

# Test for Multiplication
print('Test for multiplication:')
calculator_instance.multiply(10,10) == 100
calculator_instance.multiply(100,1) == 100
print(type(calculator_instance.multiply(1,1)) == int)

# Test for Division
print('Test for division:')
calculator_instance.divide(10,10) == 20
calculator_instance.divide(100,1) == 100
print(type(calculator_instance.divide(1,1)) == float or int)

print('Test for last result:')
# Test if last result was recorded
calculator_instance.divide(100,1) == 100
print(calculator_instance.last_result == 100)

