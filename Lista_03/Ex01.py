class Retangulo:    #entidade
    def __init__(self, b:float, h:float):
      self.__b=b
      self.__h=h

    def getBase(self) -> float:   ## Lê e retorna um atributo
      return self.__b
    def getAltura(self) -> float:  ## Lê e retorna um atributo
       return self.__h

    def setBase(self, valor_b: float):    ##Altera/Define o atributo, podendo validar antes
        if valor_b<0:
            raise ValueError("O valor da base não pode ser negativo!")
        self.__b=valor_b
    def setAltura(self, valor_h: float):    ##Altera/Define o atributo, podendo validar antes
        if valor_h<0:
            raise ValueError("O valor da altura não pode ser negativo!")
        self.__h=valor_h

    def calcular_area(self) -> float:
        return self.__b*self.__h

    def diagonal(self) -> float:
        return (self.__h**2+self.__b**2)**0.5

    def __str__(self):
        return f"Base = {self.__b} ; Altura = {self.__h}"
        
class UI: #interface com usuário
    @staticmethod
    def main():
        x=Retangulo(5.0, 8.0)
        print("--- Dados do Retângulo ---")
        print(f"Diagonal: {x.diagonal():.2f}")
        print(f"Área: {x.calcular_area():.2f}")
        print(x.__str__())
UI.main()