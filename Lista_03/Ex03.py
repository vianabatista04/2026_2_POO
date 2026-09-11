##Encapsula o número decimal e a lógica de conversão
class Conversor:    #entidade ->Cuida das regras e dados
    def __init__(self, num:int):
      self.__n=num
##Encapsulamento
    def getNum(self) -> int:  ## Lê e retorna um atributo
       return self.__n

    def setNum(self, valor_n: int):    ##Altera/Define o atributo, podendo validar antes
        if valor_n<0:
            raise ValueError("O valor do número não pode ser negativo!")
        self.__n=valor_n
##Lógica de Conversão
    def Binario(self) -> str:
        if self.__n==0:
            return "0"
        num= self.__n
        binario = ""
        while num > 0:
            resto = num%2
            binario = str(resto)+binario
            num = num //2
        return binario

    def __str__(self):
        return f"Número Decimal = {self.__n}; Número Binário = {self.Binario()}"
        
class UI: #interface com usuário ->interação e exibição
    @staticmethod
    def main():
        x=Conversor(10)
        print("--- Dados do Conversor Binário ---")
        print(f"Binário: {x.Binario()}")
        print(x.__str__())
UI.main()
