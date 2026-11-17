import json
from Model.Comercio.venda import Venda

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