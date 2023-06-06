def analizer(name):
    f = open(name)
    n = 0
    for i in f: 
        for k in i:
            if k == 'a':
                n+=1
                if n > 5:
                    print(i)  
        n=0  
analizer()