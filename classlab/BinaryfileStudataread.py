# WAP to read the data from binary file whose marks greater than 81.

import pickle
f=open('Stu.dat','rb')
try:
    while True:
        s=pickle.load(f)
        if s[2]>81:
            print(s)

except EOFError:
    pass
f.close()
