pares=[2,4,6,8,10]
for i in range(1,11):
    pares_=[]
    for p in pares:
        if p<=i:
            pares_.append(p)
    print(i,*pares_)