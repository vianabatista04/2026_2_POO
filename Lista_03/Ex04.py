##Encapsula o número decimal e a lógica de conversão
class Equacao:    #entidade ->Cuida das regras e dados
    def __init__(self, a:float, b:float, c:float):
      if a == 0:
          raise ValueError("O valor de 'a' não pode ser zero!")
      self.__na=a
      self.__nb=b
      self.__nc=c
##Encapsulamento
    def getA(self) -> float:  ## Lê e retorna um atributo
       return self.__na
    def getB(self) -> float:  ## Lê e retorna um atributo
       return self.__nb
    def getC(self) -> float:  ## Lê e retorna um atributo
       return self.__nc

    def setA(self, valor_na: float):    ##Altera/Define o atributo, podendo validar antes
        if valor_na==0:
            raise ValueError("O valor de 'a' não pode ser zero!")
        self.__na=valor_na
    def setB(self, valor_nb: float):    ##Altera/Define o atributo, podendo validar antes
        self.__nb=valor_nb
    def setC(self, valor_nc: float):    ##Altera/Define o atributo, podendo validar antes
        self.__nc=valor_nc
##Lógica de Conversão
    ##Calculo do delta
    def Delta(self) -> float:     
        return self.__nb**2-(4*self.__na*self.__nc)
    ##Verificação das raízes reais
    def TemRaizesReais(self) -> bool:
        return self.Delta()>=0
    ##Cálculo das raízes     
    def Raiz1(self) -> float:
        if self.TemRaizesReais():
            return  (-(self.__nb)+(self.Delta()**0.5))/(2*self.__na)
        return None    
    def Raiz2(self) -> float:     
        if self.TemRaizesReais():
            return  (-(self.__nb)-(self.Delta()**0.5))/(2*self.__na)
        return None    

    def __str__(self):
        if self.TemRaizesReais():
            return f"Coeficiente A= {self.__na};Coeficiente B= {self.__nb};Coeficiente C= {self.__nc} | Delta= {self.Delta()} | Raiz 1= {self.Raiz1()} | Raiz 2= {self.Raiz2()};"
        return f"Coeficiente A= {self.__na};Coeficiente B= {self.__nb};Coeficiente C= {self.__nc} | Delta= {self.Delta()} (Sem raízes reais)"
class UI: #interface com usuário ->interação e exibição
    @staticmethod
    def main():
        x=Equacao() #números separados por ,
        print("--- Dados da Equação ---")
        print(x)
        print(f"Delta: {x.Delta()}")
        print(f"Raiz 1: {x.Raiz1()}")
        print(f"Raiz 2: {x.Raiz2()}")
        
UI.main()