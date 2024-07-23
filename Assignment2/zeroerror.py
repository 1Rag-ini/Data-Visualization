# Handle ZeroDivisionError.

num=float(input('Enter the numerator::'))
den=float(input('Enter the denominator::'))
try:
    result=num/den
    print(result)
except ZeroDivisionError:
    print('Division by Zero is not allowed')

