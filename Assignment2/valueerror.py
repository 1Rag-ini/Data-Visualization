# HandleValueError.

try:
    num=int(input('Enter a number::'))
    print(f'Entered integer number is::{num}')
except ValueError:
    print('Error:Invalid Input.Please enter a valid Integer.')
