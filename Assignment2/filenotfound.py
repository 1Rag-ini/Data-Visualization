# Handle FileNotFoundError.

def file(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f'The File {filename} does not exist.')

file('ABC.txt')
file('dfg.txt')
