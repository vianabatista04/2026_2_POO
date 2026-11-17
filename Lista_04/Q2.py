class Cliente:
    def __init__(self,nome,cpf,limite):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_limite(limite)
        self.__socio:Cliente | None = None
    
    def set_nome(self,nome):
        if nome=="": raise ValueError("Nome deve ser informado")
        self.__nome=nome
    def set_cpf(self,cpf):
        if cpf=="": raise ValueError("CPF deve ser informado")
        self.__cpf=cpf
    def set_limite(self,limite):
        if limite<0: raise ValueError("Limite deve ser positivo")
        self.__limite=limite
    
    def set_socio(self,c):
        if self.__socio is not None:
            self.__socio.__socio=None
        if c is not None and c.__socio is not None:
            c.__socio.__socio =None
        self.__socio=c
        
        if c is not None:
            c.__socio = self

    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_limite(self):
        if self.__socio is None: return self.__limite
        return self.__limite + self.__socio.__limite
    def get_socio(self): return self.__socio
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__limite:.2f} - {self.get_limite():.2f}"

class Empresa:
    def __init__(self, nome: str):
        self.set_nome(nome)
        self.__clientes = []

    def set_nome(self, nome: str):
        if nome== "":
            raise ValueError("Nome da empresa deve ser informado!")
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def Inserir(self, c: Cliente):
        self.__clientes.append(c)

    def Listar(self):
        return self.__clientes

    def __str__(self):
        return f"Empresa: {self.__nome} ({len(self.__clientes)} cliente(s))"

class UI:
    empresas = []

    @staticmethod
    def main():
        op = 0
        while op != 5:
            try:
                op = UI.menu()
                if op == 1: UI.cadastrar_empresa()
                elif op == 2: UI.cadastrar_cliente()
                elif op == 3: UI.associar_socios()
                elif op == 4: UI.listar_tudo()
                elif op == 5: print("Finalizando!")
                else: print("Opção inválida!")
            except ValueError as e:
                print(f"Erro: {e}")

    @staticmethod
    def menu():
        print("1 - Cadastrar Empresa, 2 - Cadastrar Cliente, 3 - Associar Sócios, 4 - Listar Empresas e Clientes, 5 - Fim ")
        return int(input("Escolha uma opção: "))


    @classmethod
    def escolher_empresa(cls):
        if not cls.empresas:
            print("Nenhuma empresa cadastrada!")
            return None
        
        for idx, emp in enumerate(cls.empresas, 1):
            print(f"{idx} - {emp.get_nome()}")
        
        op = int(input("Selecione o número da empresa: ")) - 1
        if 0 <= op < len(cls.empresas):
            return cls.empresas[op]
        raise ValueError("Empresa inválida!")

    @classmethod
    def cadastrar_empresa(cls):
        nome = input("Informe o nome da empresa: ")
        emp = Empresa(nome)
        cls.empresas.append(emp)
        print("Empresa cadastrada com sucesso!\n")

    @classmethod
    def cadastrar_cliente(cls):
        emp = cls.escolher_empresa()
        if emp is None: return

        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        limite = float(input("Limite de crédito: "))

        cliente = Cliente(nome, cpf, limite)
        emp.Inserir(cliente)
        print("Cliente cadastrado com sucesso!\n")

    @classmethod
    def associar_socios(cls):
        emp = cls.escolher_empresa()
        if emp is None: return

        clientes = emp.Listar()
        if len(clientes) < 2:
            print("São necessários pelo menos 2 clientes na empresa para criar uma sociedade!\n")
            return

        for idx, cli in enumerate(clientes, 1):
            print(f"{idx} - {cli.get_nome()} (CPF: {cli.get_cpf()})")

        idx1 = int(input("Selecione o 1º cliente: ")) - 1
        idx2 = int(input("Selecione o 2º cliente: ")) - 1

        if idx1 == idx2:
            print("Um cliente não pode ser sócio dele mesmo!\n")
            return

        c1 = clientes[idx1]
        c2 = clientes[idx2]

        c1.set_socio(c2)
        print(f"Sociedade estabelecida entre {c1.get_nome()} e {c2.get_nome()}!\n")

    @classmethod
    def listar_tudo(cls):
        if not cls.empresas:
            print("\nNenhuma empresa cadastrada.\n")
            return

        for emp in cls.empresas:
            print(f"\n==============================")
            print(emp)
            print("------------------------------")
            clientes = emp.Listar()
            if not clientes:
                print("Sem clientes cadastrados.")
            else:
                for cli in clientes:
                    print(cli)
        print()
