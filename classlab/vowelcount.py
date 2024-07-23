# Count Vowel and Constants.


file=open('ABC.txt','r')
vlist=list('aeiouAEIOU')
vc=0
c=0
x=file.read()
for y in x:
    if (y in vlist):
        vc+=1
    else:
        c+=1
print('Total Vowels::',vc)
print('Total Constants::',c)
file.close()
