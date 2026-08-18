numeros=[]
print("Digite três valores:")
for x in range(3):
    numeros.append(int(input()))
for i in range(len(numeros)):
    ind_menor=i
    for j in range(i+1, len(numeros)):
        if numeros[j] < numeros[ind_menor]:
            ind_menor=j
    numeros[i], numeros[ind_menor]=numeros[ind_menor], numeros[i]
print(*numeros, sep=", ")