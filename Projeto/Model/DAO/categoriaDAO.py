import json
from Model.Comercio.categoria import Categoria

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
