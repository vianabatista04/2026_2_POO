import json
from Cliente import Cliente
from Cliente import Venda
from Cliente import VendaItem
from Cliente import Produto
from Cliente import Categoria

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

class VendaDAO:
    _arquivo= "vendas.json"
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
        venda_existente=cls.Listar_id(obj.getId())
        if venda_existente:
            venda_existente.setD(obj.getD())
            venda_existente.setC(obj.getC())
            venda_existente.setT(obj.getT())
            venda_existente.setId_C(obj.getId_C())
            cls.Salvar()
    
    @classmethod
    def Excluir(cls,obj): 
        venda_existente=cls.Listar_id(obj.getId())
        if venda_existente:
            cls._objetos.remove(venda_existente)
            cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls._objetos=[]
        try:
            with open(cls._arquivo, mode="r", encoding="utf-8")as arquivo:
                vendas_json=json.load(arquivo)
                for obj in vendas_json:
                    c=Venda.from_json(obj)
                    cls._objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open(cls._arquivo, mode="w", encoding="utf-8") as arquivo:
            dados=[venda.to_json() for venda in cls._objetos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

class VendaItemDAO:
    _arquivo= "vendaitens.json"
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
        item_existente=cls.Listar_id(obj.getId())
        if item_existente:
            item_existente.setQtd(obj.getQtd())
            item_existente.setPreco(obj.getPreco())
            item_existente.setId_V(obj.getId_V())
            item_existente.setId_P(obj.getId_P())
            cls.Salvar()
    
    @classmethod
    def Excluir(cls,obj): 
        item_existente=cls.Listar_id(obj.getId())
        if item_existente:
            cls._objetos.remove(item_existente)
            cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls._objetos=[]
        try:
            with open(cls._arquivo, mode="r", encoding="utf-8")as arquivo:
                vendaitens_json=json.load(arquivo)
                for obj in vendaitens_json:
                    c=VendaItem.from_json(obj)
                    cls._objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open(cls._arquivo, mode="w", encoding="utf-8") as arquivo:
            dados=[vendaitens.to_json() for vendaitens in cls._objetos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

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

class CategoriaDAO:
    _arquivo= "categoria.json"
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
        categoria_existente=cls.Listar_id(obj.getId())
        if categoria_existente:
            categoria_existente.setDesc(obj.getDesc())
            cls.Salvar()
    
    @classmethod
    def Excluir(cls,obj): 
        categoria_existente=cls.Listar_id(obj.getId())
        if categoria_existente:
            cls._objetos.remove(categoria_existente)
            cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls._objetos=[]
        try:
            with open(cls._arquivo, mode="r", encoding="utf-8")as arquivo:
                categoria_json=json.load(arquivo)
                for obj in categoria_json:
                    c=Categoria.from_json(obj)
                    cls._objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open(cls._arquivo, mode="w", encoding="utf-8") as arquivo:
            dados=[categoria.to_json() for categoria in cls._objetos]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
