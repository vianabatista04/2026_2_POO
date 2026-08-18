numeros=[]
print("Digite quatro valores inteiros")
for i in range(4):
    numeros.append(int(input()))
if len(numeros)==len(set(numeros)):
    maior=max(numeros)
    menor=min(numeros)
    soma_segundos=sum(numeros) - maior - menor
    print("Maior valor =",maior)
    print("Menor valor =", menor)
    print("A soma do segundo maior valor com o segundo menor =",soma_segundos)
else:
    print("Erro, tem valores repetidos!")