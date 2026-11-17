import json
from Model.Comercio.vendaitem import VendaItem

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