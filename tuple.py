t=(45,56,78,29,56,78,98,28,120,200)
print("Display the whole tuple.")
print(t)
print("Display the whole tuple without formatting.")
print(*t)
print("Display all element of tuple one by one.")
for element in t:
    print(element)
print("Display all element of tuple one by one in single line.")
for element in t:
    print(element,end=',')
print("\nThe fifth element of tuple form starting::",t[4])
print("The fourth element of tuple from last::",t[-4])
print("The tuple is::",t)
print("Display elements of tuple in forward direction using backward index")
for index in range(-len(t),0):
    print(t[index],end=',')
print("\nDisplay elements of tuple in backward direction using forward index")
for index in range(len(t)-1,-1,-1):
    print(t[index],end=',')
print("\nTo display the sum of elements of tuple.")
print("The tuple is::",t)
add=0
for element in t:
    add+=element
print("The sum of all elements::",add)

