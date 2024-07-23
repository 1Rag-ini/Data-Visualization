# Count uppercase characters in "ABC.txt".

def countupper(file):
    with open(file,'r') as f:
        text=f.read()
        upper=sum(1 for char in text if char.isupper())
        print(f'Total Uppercase Characters ::{upper}')

countupper('ABC.txt')
