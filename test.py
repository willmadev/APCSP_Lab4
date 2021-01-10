import resources

a = resources.read_file('test.txt')
b = resources.read_file('outputs/long.txt')

if a == b:
    print(True)
else:
    print(False)