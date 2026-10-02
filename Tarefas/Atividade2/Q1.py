from datetime import datetime , timedelta

class Treino:
    def __init__(self,id,data,distancia,tempo):
        self.setId(id)
        self.setData(data)
        self.setDistancia(distancia)
        self.setTempo(tempo)

    def getId(self):
        return self.__id
    def setId(self,id):
        if not id or id<=0:
            raise ValueError("O ID precisa ser um número maior que 0!")
        self.__id=id

    def getData(self):
        return self.__data
    def setData(self,data):
        if not data :
            raise ValueError("A data não pode ser vazia!")
        self.__data=data

    def getDistancia(self):
        return self.__distancia
    def setDistancia(self,distancia):
        if distancia is None or distancia <=0:
            raise ValueError("A distância deve ser maior que zero!")
        self.__distancia=float(distancia)

    def getTempo(self):
        return self.__tempo
    def setTempo(self,tempo):
        if  not tempo or tempo.total_seconds()<=0:
            raise ValueError("O tempo da corrida tem que ser maior que zero!")
        self.__tempo=tempo

    def pace(self):
        pace_km=self.__tempo/self.__distancia
        total_s=pace_km.total_seconds()
        minutos=int(total_s//60)
        segundos=int(total_s%60)
        return f"{minutos}'{segundos:02d}\"/km"

    def __str__(self):
        data_arrumada = self.__data.strftime("%d/%m/%Y")
        return f"Treino: {self.getId()} \n Data: {data_arrumada} \n Distância: {self.getDistancia():.2f} km \n Tempo: {self.getTempo()} \n Pace: {self.pace()}"

class TreinoUI:
    treinos=[]
    @staticmethod
    def main():
        op=0
        while op !=7:
            op=TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            elif op == 2: TreinoUI.listar()
            elif op == 3: TreinoUI.listar_id()
            elif op == 4: TreinoUI.atualizar()
            elif op == 5: TreinoUI.excluir()
            elif op == 6: TreinoUI.maisRapido()
            elif op == 7: print("Finalizando")
            else: print("Opção Inválida! Escolha um valor de 1 até 7")
    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar, 3 - Listar por Id, 4 - Atualizar, 5 - Excluir, 6 - Encontrar, 7 - Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError: return 0

    @staticmethod
    def inserir():
        print("==== Novo Treino ====")
        try:
            id=int(input("ID: "))
            data_txt=input("Data (DD/MM/AAAA): ")
            data=datetime.strptime(data_txt, "%d/%m/%Y")
            distancia=float(input("Distância(km): "))
            minutos=int(input("Tempo(min): "))
            segundos=int(input("Tempo(seg): "))
            tempo=timedelta(minutes=minutos, seconds=segundos)

            novo_treino=Treino(id,data,distancia,tempo)
            TreinoUI.treinos.append(novo_treino)
            print("Treino cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")


    @staticmethod
    def listar():
        print("==== Lista de Treino ====")
        if not TreinoUI.treinos:
            print("Nenhum treino cadastrado")
            return
        for treino in TreinoUI.treinos:
            print(treino)

    @staticmethod
    def listar_id():
        print("\n==== Busca de Treino pelo ID ====")
        try:
            id_busca = int(input("Digite o ID buscado: "))
            for treino in TreinoUI.treinos:
                if treino.getId() == id_busca:
                    print("Treino encontrado:")
                    print(treino)
                    return
            print("Treino não encontrado!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!")

    @staticmethod
    def atualizar():
        print("\n==== Atualizar Treino ====")
        try:
            id_busca = int(input("Digite o ID para ser alterado: "))
            for treino in TreinoUI.treinos:
                if treino.getId() == id_busca:
                    print("Insira os novos dados:")
                    data_txt = input("Data (DD/MM/AAAA): ")
                    nova_data = datetime.strptime(data_txt, "%d/%m/%Y")
                    nova_distancia = float(input("Nova Distância(km): "))
                    minutos = int(input("Tempo(min): "))
                    segundos = int(input("Tempo(seg): "))
                    novo_tempo = timedelta(minutes=minutos, seconds=segundos)

                    treino.setData(nova_data)
                    treino.setDistancia(nova_distancia)
                    treino.setTempo(novo_tempo)
                    print("Treino modificado!")
                    return
            print("Treino não encontrado com esse ID!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")

    @staticmethod
    def excluir():
        print("\n==== Excluir Treino ====")
        try:
            id_busca = int(input("Digite o ID para ser excluído: "))
            for treino in TreinoUI.treinos:
                if treino.getId() == id_busca:
                    TreinoUI.treinos.remove(treino)
                    print("Treino excluído!")
                    return
            print("Treino não encontrado com esse ID!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!")

    @staticmethod
    def maisRapido():
        print("==== Melhor Pace ====")
        if not TreinoUI.treinos:
            print("Nenhum treino cadastrado!")
            return
        rapido=TreinoUI.treinos[0]
        menor_pace=rapido.getTempo()/rapido.getDistancia()
        for treino in TreinoUI.treinos:
            pace=treino.getTempo()/treino.getDistancia()
            if pace<menor_pace:
                menor_pace=pace
                rapido=treino
        print("O treino com o melhor pace foi: ")
        print(rapido)

if __name__=="__main__":
    TreinoUI.main()