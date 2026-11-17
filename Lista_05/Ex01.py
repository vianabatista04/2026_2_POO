from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome precisa ser informado")
        self.__nome=nome
    def set_cpf(self, cpf):
        if cpf == "" or len(cpf) != 11: raise ValueError("CPF precisa ser informado")
        self.__cpf=cpf
    def set_telefone(self, telefone):
        if telefone == "" or len(telefone) != 11: raise ValueError("Telefone precisa ser informado e com DDD e dígito nove na frente")
        self.__telefone=telefone
    def set_nascimento(self, nascimento):
        if nascimento== "": raise ValueError("Data de nascimento precisa ser informada")
        try:
            datetime.strptime(nascimento, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Data de nascimento deve estar no formato dd/mm/aaaa")
        self.__nascimento=nascimento

    def get_nome(self): return self.__nome
    def get_cpf(self):  return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self):   return self.__nascimento
    def get_data_nascimento(self):
        return datetime.strptime(self.__nascimento, '%d/%m/%Y')

    def __str__(self):
        return f"Nome: {self.get_nome()} | CPF: {self.get_cpf()} | Tel: {self.get_telefone()} | Nasc: {self.__nascimento} "

class UI:
    pacientes=[]
    @staticmethod
    def main():
            op = 0
            while op != 4:
                try:
                    op = UI.menu()
                    if op == 1: UI.inserir()
                    elif op == 2: UI.listar_alfab()
                    elif op == 3: UI.listar_idade()
                    elif op == 4: print("Finalizando!")
                    else: 
                        print("Opção Inválida! Digitar um número de 1 a 4")
                except ValueError as e:
                    print(f"Erro: {e}")
    
    @staticmethod
    def menu():
        print("1 - Inserir paciente, 2 - Listar pacientes cadastrados por ordem alfabética, 3 - Listar pacientes cadastrados por ordem de idade, 4 - Fim")
        return int(input("Informe a opção: "))
    
    @classmethod
    def inserir(cls):
        paciente = input("Informe o nome do paciente: ")
        cpf=input("Informe o cpf do paciente: ")
        telefone=input("Informe o telefone do paciente: ")
        nascimento=input("Informe a data de nascimento do paciente (dd/mm/aaaa): ")
        x = Paciente(paciente,cpf,telefone,nascimento)    #instância da classe
        cls.pacientes.append(x)
        print("Paciente cadastrado!")
    
    @classmethod    
    def listar_alfab(cls):
        if not cls.pacientes:
            print("Nenhum paciente cadastrado")
            return
        cls.pacientes.sort(key = lambda x: x.get_nome().lower())
        print("--- Pacientes por Ordem Alfabética ---")
        for x in cls.pacientes:
            print(x)
    
    @classmethod
    def listar_idade(cls):
        if not cls.pacientes:
            print("Nenhum paciente cadastrado")
            return
        cls.pacientes.sort(key = lambda x: x.get_data_nascimento())
        print("--- Pacientes por Ordem de Idade ---")
        for x in cls.pacientes:
            print(x)
UI.main()