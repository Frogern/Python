def file():
    f = open('text2.txt')
    f = f.readlines()
    for i in f:
        line = i.split('. ')
        bug_treck= {line[0]:line[1]}
    print(bug_treck)

file()
