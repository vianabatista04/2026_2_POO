class Frete:    #entidade
    def __init__(self, distancia:float, peso:float):
      self.__d=distancia
      self.__p=peso

    def getDistancia(self) -> float:   ## Lê e retorna um atributo
      return self.__d
    def getPeso(self) -> float:  ## Lê e retorna um atributo
       return self.__p

    def setDistancia(self, valor_d: float):    ##Altera/Define o atributo, podendo validar antes
        if valor_d<0:
            raise ValueError("A distância não pode ser negativa!")
        self.__d=valor_d
    def setPeso(self, valor_p: float):    ##Altera/Define o atributo, podendo validar antes
        if valor_p<0:
            raise ValueError("O valor do peso não pode ser negativo!")
        self.__p=valor_p

    def CalcularFrete(self) -> float:
        return self.__d*self.__p*0.01

    def __str__(self):
        return f"Distância = {self.__d}; Peso = {self.__p}"
        
class UI: #interface com usuário
    @staticmethod
    def main():
        x=Frete()   #números separados por ,
        print("--- Dados do Frete ---")
        print(f"Frete: {x.CalcularFrete():.2f}")
        print(x.__str__())
UI.main()
