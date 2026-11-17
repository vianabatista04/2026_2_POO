import json
from Model.Comercio.cliente import Cliente

class ClienteDAO:
    _arquivo= "clientes.json"
    _objetos=[]
    
    @classmethod
    def Inserir(cls,obj):
        cls.Abrir()
        cls._objetos.append(obj)
        cls.Salvar()
    
    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls._objetos
    
    @classmethod
    def Listar_id(cls,id):
        cls.Abrir()
        for objeto in cls._objetos:
            if objeto.getId() == id:
                return objeto
        return None
    
    @classmethod
    def Atualizar(cls,obj):
        cliente_existente=cls.Listar_id(obj.getId())
        if cliente_existente:
            cliente_existente.setNome(obj.getNome())
            cliente_existente.setEmail(obj.getEmail())
            cliente_existente.setFone(obj.getFone())
            cls.Salvar()
    
    @classmethod
    def Excluir(cls,obj): 
        cliente_existente=cls.Listar_id(obj.getId())
        if cliente_existente:
            cls._objetos.remove(cliente_existente)
            cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls._objetos=[]
        try:
            with open(cls._arquivo, mode="r", encoding="utf-8")as arquivo:
                clientes_json=json.load(arquivo)
                for obj in clientes_json:
                    c=Cliente.from_json(obj)
                    cls._objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open(cls._arquivo, mode="w", encoding="utf-8") as arquivo:
            dados=[cliente.to_json() for cliente in cls._objetos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)