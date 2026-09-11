class Data:
    def __init__(self,dia:int,mes:int,ano:int): 
        if ano <=0:
            raise ValueError("Ano Inválido!")
        self.__a=ano
        if not(1<=mes<=12):
            raise ValueError("Mês Inválido!")
        self.__m=mes
        limite=self.dia_mes()
        if not(1<=dia<=limite):
            raise ValueError("Dia Inválido!")
        self.__d=dia

    def Bissexto(self) -> bool:
        return (self.__a%4==0 and self.__a%100!=0) or (self.__a%400==0)

    def dia_mes(self) -> int:
        dias=[31,28,31,30,31,30,31,31,30,31,30,31]
        if self.__m==2 and self.Bissexto():
            return 29
        return dias[self.__m-1]

    def getDia(self)->int:
        return self.__d

    def getMes(self)->int:
        return self.__m

    def getAno(self)->int:
        return self.__a

    def setAno(self, ano:int):
        if ano>0:
            self.__a=ano
        else:
            print("Ano Inválido!")

    def setMes(self, mes:int):
        if 1<=mes<=12:
            self.__m=mes
        else:
            print("Mês Inválido!")

    def setDia(self, dia:int):
        limite=self.dia_mes()
        if 1 <= dia <= limite:
            self.__d=dia
        else:
            print("Dia Inválido para esse mês!")

    def __str__(self):
        return f"{self.__d:02d}/{self.__m:02d}/{self.__a}"

class UI:
    @staticmethod
    def main():
        try:
            x=Data()    #numeros separados por ,
            print("----- Dados da Data -----")
            print(x)
            print(f"Dia: {x.getDia()}")
            print(f"Mês: {x.getMes()}")
            print(f"Ano: {x.getAno()}")
        except ValueError as e:
            print(f"Erro ao cadastrar data: {e}")       
UI.main()