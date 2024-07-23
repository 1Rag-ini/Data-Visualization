# Count words start with 'i'.

file=open('ABC.txt')
count=0
for line in file:
    words=line.split()
    for word in words:
        if word[0]=='i' or word[0]=='I':
            count+=1
print('Total Words start with "I"::',count)
file.close()
