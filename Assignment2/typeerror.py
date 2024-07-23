# Handle TypeError.

try:
    num1=float(input('Enter first number::'))
    num2=float(input('Enter second number::'))
    print(f'Entered numbers are::{num1} and {num2}')
except ValueError:
    print("Please enter the valid numerical values.") 
