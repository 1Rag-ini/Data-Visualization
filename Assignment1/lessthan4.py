# Display words with less than 4 characters from "Story.txt".

def display(file):
    with open(file,'r') as f:
        text=f.read()
        words=text.split()
        short=[word for word in words if len(word)<4]
        print("Words with less than 4 characters::")#,short)
        for word in short:
            print(word)

display('Story.txt')
