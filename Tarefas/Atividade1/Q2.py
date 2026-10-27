class Viagem:
    def __init__(self, destino:str, distancia:float, litros:float):
        self.setDest(destino)
        self.setDist(distancia)
        self.setLt(litros)

    def getDest(self):
        return self.__dest
    
    def getDist(self):
        return self.__dist
    
    def getLt(self):
        return self.__lt
    
    def setDest(self, destino):
        if destino is None or str(destino).strip()=="":
            raise ValueError("O destino não pode ser vazio!")
        self.__dest=str(destino).strip()
    
    def setDist(self, distancia):
        if distancia is None or distancia<=0:
            raise ValueError("A distância não pode ser negativa ou zero")
        self.__dist=distancia
    
    def setLt(self, litros):
        if litros is None or litros<=0:
            raise ValueError("A quantidade de litros não pode ser negativa ou vazia!")
        self.__lt=litros

    def consumo(self):
        return self.__dist/self.__lt

    def __str__(self):
        return f"Destino: {self.__dest}  |  Distância: {self.__dist:.1f} Km  |  Litros: {self.__lt:.1f} L "

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
        print("==== Cadastro da Viagem ====")
        try:
            destino=input("Informe o destino: ")
            distancia=float(input("Informe a distância(km): "))
            litros=float(input("Informe a quantidade de litros usada(L): "))
            viagem=Viagem(destino,distancia,litros)
            print("Dados da Viagem Registrados:")
            print(viagem)
            print(f"Consumo Médio: {viagem.consumo():.2f} km/l")
        except ValueError as e:
            print(f"Erro no cadastro: {e}")
UI.main()
    