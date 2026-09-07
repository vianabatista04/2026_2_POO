def Diagonal(b,h):
    diagonal=(b**2 + h**2)**0.5
    return diagonal

largura,altura=map(int,input().split())
print(Diagonal(largura,altura))