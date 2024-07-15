# To generate numbers between 10 to 100 which are divisible by 3 and 5 both.
print("Generate the numbers between 10 to 100 which is divisible by 3 and 5 both")
for x in range(10,100):
    if(x%3==0 and x%5==0):
        print(x,end=",")

print("---------------------------------------------------")
#To generate numbers between 50 to 1000 which is multiples of 4 by using while loop.
print("Generate the numbers between 50 to 1000 which is multiple of 4")
x=50
while(x<1000):
    if(x%4==0):
        print(x,end=",")
    x+=1

print("---------------------------------------------------")
#Perform tasks on list.
#create list of 20 elements and display the list using forward indexing in reverse order.
lst=list(range(1,21))
for x in range(len(lst)-1,-1,-1):
    print(lst[x])
#for x in range(len(lst)):
#    print(lst[len(lst)-x-1])

print("---------------------------------------------------")
#print the list using backward indexing.
lst1=[22,30,"Hii",45,55]
for x in range(-len(lst1),0):
    print(lst1[x])

print("---------------------------------------------------")
#To insert one element at end of list.
lst2=[10,20,30,40]
print(lst2)
y=int(input("Enter the one element::"))
lst2.append(y)
print("New list after adding",y,"at end")
print(lst2)

print("---------------------------------------------------")
#To insert multiple element at end of list.
lst3=[20,25,40,50]
print(lst3)
lst3.extend(lst1)
print("New list after adding",lst1,"at end of",lst3)
print(lst3)

print("---------------------------------------------------")
#To insert new element at 4th position in  list.
print(lst2)
z=int(input("Enter the number to add it in 4th position of list::"))
lst2.insert(3,z)
print("List after adding element at 4th position")
print(lst2)
