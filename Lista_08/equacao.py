class Equacao:
    def __init__(self,a,b,c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def set_a(self,a):
        if a ==0:
            raise ValueError("Valor de a precisa ser diferente de 0")
        self.__a=a
    def set_b(self,b):
        self.__b=b
    def set_c(self,c):
        self.__c=c

    def Delta(self):
        return (self.__b**2)-4*self.__a*self.__c

    def Y(self,x):
        return self.__a * (x**2) + self.__b * x + self.__c

    def X1(self):
        if self.Delta()<0:
            return "Não possui raiz real"
        return (-(self.__b)+(self.Delta()**0.5))/(2*self.__a)
    
    def X2(self):
        if self.Delta()<0:
            return "Não possui raiz real"
        return (-(self.__b)-(self.Delta()**0.5))/(2*self.__a)
    
    def __str__(self):
        return f"Delta: {self.Delta()} | Raiz X1: {self.X1()} | Raiz X2: {self.X2()}"
    
