# create a dataset using Dictionary.
lststu=[]
lststu.append({'stdid':"std001",'stdname':"Aryan",'standard':"10th",'age':16,'hindi':76,'english':67,'maths':78,'science':79,'computer':89,'total':389})
lststu.append({'stdid':"std002",'stdname':"Banni",'standard':"10th",'age':15,'hindi':78,'english':79,'maths':89,'science':92,'computer':95,'total':433})
lststu.append({'stdid':"std003",'stdname':"Peter",'standard':"10th",'age':17,'hindi':68,'english':78,'maths':88,'science':95,'computer':92,'total':421})
lststu.append({'stdid':"std004",'stdname':"Bheem",'standard':"10th",'age':18,'hindi':78,'english':67,'maths':65,'science':82,'computer':85,'total':377})
lststu.append({'stdid':"std005",'stdname':"Jerry",'standard':"10th",'age':16,'hindi':50,'english':55,'maths':60,'science':65,'computer':70,'total':300})
lststu.append({'stdid':"std006",'stdname':"Jaggu",'standard':"10th",'age':16,'hindi':66,'english':78,'maths':87,'science':67,'computer':77,'total':375})
lststu.append({'stdid':"std007",'stdname':"Harry",'standard':"10th",'age':18,'hindi':60,'english':65,'maths':70,'science':75,'computer':80,'total':350})
lststu.append({'stdid':"std008",'stdname':"Sunny",'standard':"10th",'age':19,'hindi':76,'english':79,'maths':80,'science':82,'computer':85,'total':402})
lststu.append({'stdid':"std009",'stdname':"Rishi",'standard':"10th",'age':17,'hindi':67,'english':80,'maths':85,'science':95,'computer':78,'total':405})
lststu.append({'stdid':"std010",'stdname':"Kashi",'standard':"10th",'age':16,'hindi':78,'english':80,'maths':90,'science':79,'computer':76,'total':403})
#print(lststu)
print("|-------------------------------------------------------------------------|")
print("| Stuid  | Stuname|Standard|Age|Hindi|English|Maths|Science|Computer|Total|")
print("|-------------------------------------------------------------------------|")
for stu in lststu:
    print('|',stu['stdid'],'|',stu['stdname'],' | ',stu['standard'],' |',stu['age'],'|',stu['hindi'],' | ',stu['english'],' | ',stu['maths'],' | ',stu['science'],' | ',stu['computer'],' | ',stu['total'],' |')
print("|-------------------------------------------------------------------------|")

#for element in lststu:
#    print(element['stdid'])
# Display the name of students whose marks is greater than 50 in english.
print('Display the name of students whose marks is greater than 50 in english.')
print('|-------|')
print('|stdname|')
print('|-------|')
for element in lststu:
    if (element['english']>50):
        print('|',element['stdname'],'|')
print('|-------|')

# Display the name and age of students who are top 4 scorer of maths.
print('Display the name and age of students who are top 4 scorer of maths.')
print('|------------|')
print('|stdname| age|')
print('|------------|')
maxmarks=[]
for element in lststu:
    maxmarks.append(element['maths'])
maxmarks.sort(reverse=True)
for i in range(0,4):
    for element in lststu:
        if (maxmarks[i]==element['maths']):
            print('|',element['stdname'],'|',element['age'],'|')
print('|------------|')
        
print('Display the id,name and age of students who are bottom 3 scorer of computer.')
print('|---------------------|')
print('| stdid  |stdname| age|')
print('|---------------------|')
maxmarks=[]
for element in lststu:
    maxmarks.append(element['computer'])
maxmarks.sort()
for i in range(0,3):
    for element in lststu:
        if (maxmarks[i]==element['computer']):
            print('|',element['stdid'],'|',element['stdname'],'|',element['age'],'|')
print('|---------------------|')
