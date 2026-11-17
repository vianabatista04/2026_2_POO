import enum
from datetime import datetime, timedelta

class Turno(enum.Enum):
    Matutino = 1
    Vespertino = 2
    Noturno = 3
class Cargo(enum.Enum):
    Estagiário = 1
    Analista = 2
    Gerente = 3
    Diretor = 4

class Funcionario:
    def __init__(self, nome, matricula, salario, cargo, turno, data_admissao):
        self.set_nome(nome)
        self.set_matricula(matricula)
        self.set_salario(salario)
        self.set_cargo(cargo)
        self.set_turno(turno)
        self.set_data_admissao(data_admissao)

    def get_nome(self): return self.__nome
    def get_matricula(self): return self.__matricula
    def get_salario(self): return self.__salario
    def get_cargo(self): return self.__cargo
    def get_turno(self): return self.__turno
    def get_data_admissao(self): return self.__data_admissao
    
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome=nome
    def set_matricula(self, matricula):
        if matricula == "": raise ValueError("Matrícula deve ser informada")
        self.__matricula=matricula
    def set_salario(self, salario):
        if salario < 0: raise ValueError("Salário não pode ser negativo!")
        self.__salario=float(salario)
    def set_cargo(self, cargo):
            if cargo == "": raise ValueError("Cargo deve ser informado")
            self.__cargo=cargo
    def set_turno(self, turno):
            if turno == "": raise ValueError("Turno deve ser informado")
            self.__turno=turno
    def set_data_admissao(self, data_admissao):
            if data_admissao == "": raise ValueError("Data de admissão deve ser informada")
            if type(data_admissao)==str: self.__data_admissao= datetime.strptime(data_admissao, '%d/%m/%Y')
            else:
                self.__data_admissao=data_admissao
        
    def TempoTrabalho(self):
        agora=datetime.now()
        dif=agora- self.__data_admissao
        dias=dif.days
        if dias<0:
            return "Data de admissão de horas"
        anos= dias//365
        meses=(dias%365)//30
        return f"{anos} anos(s) e {meses} mês(es) ({dias} dias)"

    def Promover(self):
        prox_valor=self.__cargo.value+1
        if prox_valor<=len(Cargo):
            self.__cargo=Cargo(prox_valor)
            self.__salario=self.__salario*1.25
            print(f"Funcionário promovido para {self.__cargo.name}! Novo salário: R${self.__salario:.2f}")
        else:
            print(f"{self.__nome} já está no cargo máximo ({self.__cargo.name}) e não pode ser promovido!")

    def __str__(self):
        data=self.__data_admissao.strftime("%d/%m/%Y")
        return f"Matrícula: {self.__matricula} | Nome: {self.__nome} | Cargo: {self.__cargo.name} | Turno: {self.__turno.name} | Salário: R${self.__salario:.2f} | Admissão: {data}"

class UI:
    funcionarios=[]
    @staticmethod
    def main():
        op = 0
        while op != 5:
            try:
                op = UI.menu()
                if op == 1: UI.inserir()
                elif op == 2: UI.listar()
                elif op == 3: UI.promover()
                elif op == 4: UI.tempo_trabalho()
                elif op == 5: print("Finalizando!")
                else: print("Opção Inválida!")
            except ValueError as e:
                 print(f"Erro: {e}")     
                 
    @staticmethod
    def menu():
        print("1 - Cadastrar Funcionário, 2 - Listar Funcionários, 3 - Promover Funcionários, 4 - Ver Tempo Trabalhado, 5 - Fim")
        return int(input("Informe a opção: "))

    @classmethod
    def escolher_cargo(cls):
        for cargo in Cargo:
            print(f"{cargo.value} - {cargo.name}")
        op = int(input("Escolha o número do cargo: "))
        return Cargo(op)

    @classmethod
    def escolher_turnos(cls):
        print("1 - Matutino, 2 - Vespertino, 3 - Noturno")
        turno_selec=[]
        while True:
            op=int(input("Digite o número do turno ou 0 para encerrar a seleção:"))
            if op==0:
                 if len(turno_selec) == 0:
                      print("Selecione pelo menos um turno!")
                      continue
                 break
            elif op in [1,2,3]:
                turno_obj=Turno(op)
                if turno_obj not in turno_selec:
                    turno_selec.append(turno_obj)
                else:
                    print("Turno já selecionado!")
            else:
                 print("Opção de turno inválida!")
        return turno_selec

    @classmethod
    def inserir(cls):
        nome=input("Informe o nome: ")
        matricula=input("Informe o matrícula: ")
        salario=float(input("Informe o salário: "))
        cargo=cls.escolher_cargo()
        turno=cls.escolher_turnos()
        data_adm=input("Informe a data de admissão (dd/mm/aaaa): ")
        f=Funcionario(nome,matricula,salario,cargo,turno,data_adm)
        cls.funcionarios.append(f)
        print("Funcionário cadastrado!")

    @classmethod
    def listar(cls):
        if not cls.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        for f in cls.funcionarios:
             print(f)

    @classmethod
    def promover(cls):
        mat=input("Informe a matrícula do funcionário para ser promovido: ")    
        for f in cls.funcionarios:
            if f.get_matricula() == mat:
                f.Promover()
                return
        print("Funcionário não encontrado!")

    @classmethod
    def tempo_trabalho(cls):
        mat=input("Informe a matrícula do funcionário: ")
        for f in cls.funcionarios:
             if f.get_matricula()==mat:
                  print(f"Tempo de trabalho de {f.get_nome()}: {f.TempoTrabalho()}")
                  return
        print("Funcionário não encontrado!") 
UI.main()