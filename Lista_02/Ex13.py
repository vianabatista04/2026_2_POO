def RemoverEspacos(texto):
    palavras=texto.split()
    texto_certo=" ".join(palavras)
    return texto_certo

frase=input()
print(RemoverEspacos(frase))