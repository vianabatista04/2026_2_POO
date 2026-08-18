impar=[]
par=[]
print("Digite quatro valores inteiros")
for i in range(4):
    valor=int(input())
    if valor%2==0:
        par.append(valor)
    else:
        impar.append(valor)
print("Soma dos pares =",sum(par))
print("Soma dos ímpares =",sum(impar))