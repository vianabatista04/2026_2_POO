print("Digite uma frase:")
frase=input().strip()
new_frase=frase
while True:
    if len(new_frase)>1:
        new_frase=new_frase[1:] + new_frase[0]
        print(new_frase)
    if new_frase==frase:
        break