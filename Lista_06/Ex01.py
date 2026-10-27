import json

class Cliente:
    def __init__(self,id,nome,email,telefone):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setFone(telefone)
        
    def getId(self):
        return self._id
    def setId(self,id):
        if not id or id<=0:
            raise ValueError("O ID precisa ser um número maior que 0!")
        self._id=id
    
    def getNome(self):
        return self._nome
    def setNome(self,nome):
        if not nome :
            raise ValueError("O nome não pode ser vazio!")
        self._nome=nome

    def getEmail(self):
        return self._email
    def setEmail(self,email):
        if not email :
            raise ValueError("O email não pode ser vazio!")
        self._email=email
    
    def getFone(self):
        return self._fone    
    def setFone(self, fone):
        if fone == "" or len(fone) != 11: raise ValueError("Telefone precisa ser informado e com DDD e dígito nove na frente")
        self._fone=fone
    
    def __str__(self):
        return f"ID: {self.getId()} | Nome: {self.getNome()} | Email: {self.getEmail()} | Fone: {self.getFone()} "
    
    def to_dict(self):
        return {
            "id": self._id,
            "nome": self._nome,
            "email": self._email,
            "telefone": self._fone
        }
    
class ClienteDAO:
    objetos=[]
    
    @classmethod
    def inserir(cls,obj):
        cls.objetos.append(obj)
    
    @classmethod
    def listar(cls):
        return cls.objetos
    
    @classmethod
    def listar_id(cls,id):
        for objeto in cls.objetos:
            if objeto.getId() == id:
                return objeto
        return None
    
    @classmethod
    def atualizar(cls,obj):
        cliente_existente=cls.listar_id(obj.getId())
        if cliente_existente:
            cliente_existente.setNome(obj.getNome())
            cliente_existente.setEmail(obj.getEmail())
            cliente_existente.setFone(obj.getFone())
    
    @classmethod
    def excluir(cls,obj): 
        cliente_existente=cls.listar_id(obj.getId())
        if cliente_existente:
            cls.objetos.remove(cliente_existente)

    @classmethod
    def abrir(cls):
        try:
            with open("clientes.json", mode="r", encoding="utf-8")as arquivo:
                clientes_json=json.load(arquivo)
                cls.objetos.clear()
                for obj in clientes_json:
                    c=Cliente(obj["id"], obj["nome"], obj["email"], obj["telefone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            cls.objetos=[]

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w", encoding="utf-8") as arquivo:
            dados=[cliente.to_dict() for cliente in cls.objetos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

class ClienteUI:
    @staticmethod
    def main():
        ClienteDAO.abrir()
        op=0
        while op !=5:
            op=ClienteUI.menu()
            if op == 1: 
                ClienteUI.listar()
            elif op == 2: 
                ClienteUI.inserir()
            elif op == 3: 
                ClienteUI.atualizar()
            elif op == 4: 
                ClienteUI.excluir()
            elif op == 5: 
                ClienteDAO.salvar()
                print("Finalizando")
            else: 
                print("Opção Inválida! Escolha um valor de 1 até 5")
    
    @staticmethod
    def menu():
        print("1 - Listar, 2 - Inserir, 3 - Atualizar, 4 - Excluir, 5 - Fim ")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError: return 0
    
    @staticmethod
    def listar():
        print("==== Lista de Clientes ====")
        clientes=ClienteDAO.listar()
        if not clientes:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)
    @staticmethod
    def inserir():
        print("==== Novo Cliente ====")
        try:
            id=int(input("ID: "))
            nome=input("Nome: ")
            email=input("Email: ")
            telefone=input("Telefone (com DDD, 11 dígitos): ")
            novo_cliente=Cliente(id,nome,email,telefone)
            ClienteDAO.inserir(novo_cliente)
            print("Cliente cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def atualizar():
        print("\n==== Atualizar Informação do Cliente ====")
        try:
            id_busca = int(input("Digite o ID para ser alterado: "))
            cliente_existente=ClienteDAO.listar_id(id_busca)
            if cliente_existente is None:
                print("Cliente não encontrado com o ID informado!")
                return
            print("Informe os novos dados: ")
            nome=input("Nome: ")
            email=input("Email: ")
            telefone=input("Telefone (com DDD, 11 dígitos): ")
            atualizado=Cliente(id_busca,nome,email,telefone)
            ClienteDAO.atualizar(atualizado)
            print("Cliente Atualizado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def excluir(): 
        print("\n==== Excluir Cliente ====")
        try:
            id_busca = int(input("Digite o ID para ser excluído: "))
            cliente_existente=ClienteDAO.listar_id(id_busca)
            if cliente_existente is None:
                print("Cliente não encontrado com o ID informado!")
                return
            ClienteDAO.excluir(cliente_existente)
            print("Cliente Excluído!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!") 

ClienteUI.main()