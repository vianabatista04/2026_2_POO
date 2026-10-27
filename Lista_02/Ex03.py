class Conta:
    def __init__(self):
        self.titular="sem nome"
        self.numero="sem número"
        self.__saldo=0  #encapsulamento; dados sensíveis
    def depositar(self, valor):
        if valor >=0:
            self.__saldo += valor
        else:
            #print("Valor deve ser positivo")
            raise ValueError("Valor deve ser positivo") #gera erro e quebra o programa
    def sacar(self, valor):
        if valor >= 0 and self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo Insulficiente")
    def saldo_atual(self):
        return self.__saldo

#Interface com o usuário
class UI:
    @staticmethod
    def main():
        x=Conta()
        print(f"Titular: {x.titular}, Número da conta: {x.numero}, Saldo: {x.saldo_atual()}")
        x.titular="Maria"
        x.numero="123-0"
        print(x.titular, x.numero, x.saldo_atual())
        x.depositar(1000)
        print(x.titular, x.numero, x.saldo_atual())
        x.sacar(300)
        print(x.titular, x.numero, x.saldo_atual())
UI.main()