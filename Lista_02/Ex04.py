class EntradaCinema:
    def __init__(self,dia: str,hora:int):
        self.set_dia(dia)
        self.set_hora(hora)
    def get_dia(self):
        return self.__dia
    def get_hora(self):
        return self.__hora
    def set_dia(self, dia):
        if dia == "": raise ValueError("O dia deve ser informado!")
        self.__dia=dia.lower().strip()
    def set_hora(self, hora):
        hora = int(hora)
        if hora < 0 or hora > 23:
            raise ValueError("Horário inválido!")
        self.__hora = hora

    def inteira(self):
        if self.__dia=="quarta":
            return 8.0
        if self.__dia in ["segunda","terca","terça","quinta"]:
            valor=16.0
        else:
            valor=20.0
        if 17 <= self.__hora<=23:
            valor=valor*1.5
        return valor

    def meia(self):
        if self.__dia == "quarta":
            return 8.0
        return self.inteira()/2

class UI:
    @staticmethod
    def main():
        try:
            dia=input("Informe o dia da semana: ")
            hora=int(input("Informe o horário da sessão (0-23h): "))
            x=EntradaCinema(dia,hora)
            print(f"Sessão: {x.get.__dia.capitalize()} às {x.get.__hora}h | Inteira: R$ {x.inteira():.2f} | Meia: R$ {x.meia():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")
UI.main()