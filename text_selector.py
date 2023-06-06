def selector(name):
    f = open(name)
    n = 1
    for i in f: 
        if n % 2 == 0:
            print(i)  
        n+=1  
selector('text.txt')
