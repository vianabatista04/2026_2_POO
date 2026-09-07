def MenorInteiro(x):
    if x == int(x):
        return int(x)
    elif x>0:
        return int(x) + 1
    else:
        return int(x)

numero=float(input())
print(MenorInteiro(numero))