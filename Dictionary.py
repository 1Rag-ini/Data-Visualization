student={"Stdid":"std001",'Maths':78,'Stdname':"Rohan","Age":16}
print("Display the whole dictionary.")
print(student)
print("Display all the keys of dictionary.")
print(*student)
print("Display the value using the key of dictionary.")
#print(student['stdname'])
for element in student:
    print(student[element])
#To insert an element with key maths and value 90.
student['Maths']=90
#TO insert the new element.
student['English']=89
print(student)
student.pop('Maths')
print(student)
