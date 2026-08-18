def trimestre(num):
    meses=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    if 1<=num<=12:
        mes=meses[num-1]
        if 1<=num<=3:
            trim="primeiro trimestre"
        elif 4<=num<=6:
            trim="segundo trimestre"
        elif 7<=num<=9:
            trim="terceiro trimestre"
        elif 10<=num<=12:
            trim="quarto trimestre"
        return mes,trim
    else:
        return None,"mês inválido"

print("Informe o número do mês")
numero=int(input())
mes_,trim_=trimestre(numero)

if mes_:
    print(f"O mês de {mes_} é do {trim_} do ano")
else:
    print("Valor inválido! Há somente 12 meses no ano")