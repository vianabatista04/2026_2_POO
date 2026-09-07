def Primos(n):
    soma=0
    for valor in range(1,n+1):
        if n%valor==0:
            soma+=1
    if soma==2:
        return "Primo!"
    else:
        return "Não é Primo!"

a=int(input())
print(Primos(a))