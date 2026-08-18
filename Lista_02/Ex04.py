print("Digite uma data no formato dd/mm/aaaa")
data=str(input())
dia,mes,ano=data.split("/")
dia=int(dia)
mes=int(mes)
ano=int(ano)
if 1>dia>31 or 1>mes>12 or 1900>ano>2100:
    print("A data informada não é válida")
else:
    print("A data informada é válida")