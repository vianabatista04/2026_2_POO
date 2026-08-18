valores=list(map(int,input().split()))
ordem=sorted(valores, key=abs)
print("Resultado:",*ordem)