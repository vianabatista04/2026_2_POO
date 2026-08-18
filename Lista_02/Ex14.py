def MMC(x, y):
    maior=max(x,y)
    while True:
        if maior%x == 0 and maior%y == 0:
            mmc=maior
            break
        maior+=1
    return mmc

a,b=map(int,input().split())
print(MMC(a,b))