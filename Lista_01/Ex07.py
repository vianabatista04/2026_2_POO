print("Digite uma frase:")
frase=str(input())
palavras=frase.split()
while palavras:

    print(" ".join(palavras))
    palavras.pop(0)