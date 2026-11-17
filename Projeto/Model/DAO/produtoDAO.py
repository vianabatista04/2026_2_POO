import json
from Model.Comercio.produto import Produto

class ProdutoDAO:
    _arquivo= "produto.json"
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
        produto_existente=cls.Listar_id(obj.getId())
        if produto_existente:
            produto_existente.setDesc(obj.getDesc())
            produto_existente.setPreco(obj.getPreco())
            produto_existente.setEstq(obj.getEstq())
            produto_existente.setId_Cat(obj.getId_Cat())
            cls.Salvar()
    
    @classmethod
    def Excluir(cls,obj): 
        produto_existente=cls.Listar_id(obj.getId())
        if produto_existente:
            cls._objetos.remove(produto_existente)
            cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls._objetos=[]
        try:
            with open(cls._arquivo, mode="r", encoding="utf-8")as arquivo:
                produto_json=json.load(arquivo)
                for obj in produto_json:
                    c=Produto.from_json(obj)
                    cls._objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open(cls._arquivo, mode="w", encoding="utf-8") as arquivo:
            dados=[produto.to_json() for produto in cls._objetos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
