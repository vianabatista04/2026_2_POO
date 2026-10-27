class Pais:
    def __init__(self, nome:str, populacao:int, area:float):
        self.setNome(nome)
        self.setPop(populacao)
        self.setAr(area)

    def getNome(self):
        return self.__nome
    
    def getPop(self):
        return self.__pop
    
    def getAr(self):
        return self.__ar
    
    def setNome(self, nome):
        if str(nome).strip() == "":
            raise ValueError("O nome não pode ser vazio!")
        self.__nome=str(nome).strip()
    
    def setPop(self, populacao):
        if populacao<=0:
            raise ValueError("A população não pode ser negativa ou zero")
        self.__pop=populacao
    
    def setAr(self, area):
        if area<=0:
            raise ValueError("A quantidade de área não pode ser negativa ou zero!")
        self.__ar=area

    def densidade(self):
        return self.__pop/self.__ar

    def __str__(self):
        return f"Nome: {self.__nome}  |  População: {self.__pop} hab.  |  Área: {self.__ar:,.2f} km2 "

class UI:
    @staticmethod
    def main():
        op=0
        while op!=2:
            op=UI.menu()
            if op==1: UI.Calculo()
            elif op==2:
                print("Finalizando!")
            else:
                print("Opção Inválida! Digitar 1 ou 2")

    @staticmethod
    def menu():
        try:
            print("1 - Calcular, 2 - Fim")
            return int(input("Escolha uma opção:"))
        except ValueError:
            return 0

    @classmethod
    def Calculo(cls):
        print("==== Cadastro da País ====")
        try:
            nome=input("Informe o nome do país: ")
            populacao=float(input("Informe a população(hab): "))
            area=float(input("Informe a quantidade de área usada(km2): "))
            x=Pais(nome,populacao,area)
            print("Dados do País Registrados:")
            print(x)
            print(f"Densidade Demográfica: {x.densidade():.2f} hab/km2")
        except ValueError as e:
            print(f"Erro no cadastro: {e}")
UI.main()
    