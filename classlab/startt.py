# WAP to count no. of lines start with 't'.

file=open('Story.txt','r')
count=0
data=file.readlines()
for line in data:
    if line[0]=='T' or line[0]=='t':
        count+=1
        print(line)
print('Total lines start with "T"::',count)
file.close()
