#Lab 3

import numpy as n

# Question.1
cateogary1_revenue=n.array([500,600,700,550])
cateogary2_revenue=n.array([450,700,800,600])
total=n.sum((cateogary1_revenue,cateogary2_revenue),axis=0)
#total=cateogary1_revenue+cateogary2_revenue
print('Total revenue::',total)


# Question.2
revenue=n.array([10000,12000,11000,10500])
expenses=n.array([4000,5000,4500,4800])
profit=revenue-expenses
print('Profit::',profit)


# Question.3
inventory=n.array([10,0,5,0,20,0])
out=inventory[inventory==0]
print('Out of Stock Products::',out)


# Question.4
quantity=n.array([2,3,4,1])
price_per_item=n.array([10.0,5.0,8.0,12.0])
totalprice=quantity*price_per_item
print('Total Cost of items::',totalprice)
