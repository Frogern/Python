def file():
    f = open('text2.txt')
    f = f.readlines()
    for i in f:
        line = i.split('. ')
    print(i)

file()
