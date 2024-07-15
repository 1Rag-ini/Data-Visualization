lstheading=["Stuid","Stuname","Standard","Age","Hindi","English","Maths","Science","Computer","Total"]
lststu=[]
lststu.append(["stu001","Aryan","10th",16,76,67,78,79,89,389])
lststu.append(["stu002","Banni","10th",15,78,79,89,92,95,433])
lststu.append(["stu003","Peter","10th",17,67,78,89,95,92,421])
lststu.append(["stu004","Bheem","10th",18,78,67,65,82,85,377])
lststu.append(["stu005","Jerry","10th",16,50,55,60,65,70,300])
lststu.append(["stu006","Jaggu","10th",16,66,78,89,65,77,375])
lststu.append(["stu007","Harry","10th",18,60,65,70,75,80,350])
lststu.append(["stu008","Sunny","10th",19,76,79,80,82,85,402])
lststu.append(["stu009","Rishi","10th",17,67,80,85,95,78,405])
lststu.append(["stu010","Kashi","10th",16,78,80,90,79,76,403])
print("|-------------------------------------------------------------------------|")
print("| Stuid  | Stuname|Standard|Age|Hindi|English|Maths|Science|Computer|Total|")
print("|-------------------------------------------------------------------------|")
for stu in lststu:
    print('|',stu[0],'|',stu[1],' | ',stu[2],' |',stu[3],'|',stu[4],' | ',stu[5],' | ',stu[6],' | ',stu[7],' | ',stu[8],' | ',stu[9],' |')
print("|-------------------------------------------------------------------------|")
#Display name of student whose marks is greater than 50 in english.
print("Display name of student whose marks is greater than 50 in english.")
print('|-------|')
print('| Name  |')
print('|-------|')
for stu in lststu:
    if(stu[5]>50):
        print('|',stu[1],'|')
print('|-------|')
#Display name and age of student of top 4 scorer of Maths.
print("Display name and age of student those are top 4 scorer of Maths.")
lststu.sort(reverse=True,key=lambda x:x[6])
#lststu.sort(key=stu[6] for stu in lststu)
print('|------------|')
print('| Name  | Age|')
print('|------------|')
for stu in range(0,4):
    t=lststu[stu]
    print('|',t[1],'|',t[3],'|')
print('|------------|')
#Display Id,name and age of student those are bottom 3 scorer of computer.
print('Display Id,name and age of student those are bottom 3 scorer of computer.')
lststu.sort(key=lambda x:x[8])
print('|---------------------|')
print('| Stuid  | Name  |Age |')
print('|---------------------|')
for i in range(0,3):
    r=lststu[i]
    print('|',r[0],'|',r[1],'|',r[3],'|')
print('|---------------------|')

























#print(11,"John","B",5)
#print(12,"Tomy","A",5)
#print(13,"Annu","A",7)
#print(14,"Oggy","B",5)
#print(15,"Ashu","A",5)
#print(16,"Anni","A",6)
#print(17,"Soni","B",5)
#print(18,"Cookie","B",7)
#print(19,"Roxi","A",5)
#print(20,"Alex","A",6)
