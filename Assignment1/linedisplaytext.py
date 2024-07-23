# Read content from "ABC.txt" line by line and display on the screen.

def readline(file):
    with open(file,'r') as f:
        for line in f:
            print(line.strip())
readline('ABC.txt')
