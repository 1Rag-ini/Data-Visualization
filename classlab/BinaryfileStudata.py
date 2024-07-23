#WAP for binary file to take student records.

import pickle
with open('Stu.dat','wb') as f:
    while True:
         rollno=int(input('Enter Roll no.::'))
         name=input("Enter Name::")
         marks=int(input("Enter Marks::"))
         d=[rollno,name,marks]
         pickle.dump(d,f)
         print('Success')
         wish=input('Press y/n (y for continue & n for discontinue)::')
         if wish=='n':
               break


