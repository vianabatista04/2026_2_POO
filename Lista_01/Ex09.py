print("Digite uma frase:")
palavras=input().split()
for palavra in palavras:
    inverso=palavra[::-1]
    print(inverso)