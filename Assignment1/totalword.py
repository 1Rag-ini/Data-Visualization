# Count and display the total no. of words in "ABC>txt".

def countwords(file):
    with open(file,'r') as f:
        text=f.read()
        words=text.split()
        print(len(words))
        print(f'Total no. of words:{len(words)}')

countwords('ABC.txt')
