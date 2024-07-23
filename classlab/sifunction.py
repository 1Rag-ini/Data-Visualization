# Simple interest using function.

def si(p,r,t):
        return (p*r*t)/100

p=float(input('Enter the principal::'))
r=float(input('Enter the Rate::'))
t=float(input('Enter the Time::'))
print('Simple Interest::',si(p,r,t))
