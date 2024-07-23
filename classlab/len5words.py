# Display line which have more than 5 words.

file=open('ABC.txt')
for line in file:
    words=line.split()
    if len(words)>5:
        print(line)

file.close()

