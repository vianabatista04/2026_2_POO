class Produto:
    def __init__(self,id,descricao,preco,estoque,id_categoria=0):
        self.setId(id)
        self.setDesc(descricao)
        self.setPreco(preco)
        self.setEstq(estoque)
        self.setId_Cat(id_categoria)
        
    def getId(self):
        return self._id
    def setId(self,id):
        if not id or id<=0:
            raise ValueError("O ID precisa ser um número maior que 0!")
        self._id=id
    
    def getDesc(self):
        return self._desc
    def setDesc(self,descricao):
        if not descricao :
            raise ValueError("A descrição não pode ser vazia!")
        self._desc=descricao

    def getPreco(self):
        return self._p
    def setPreco(self,preco):
        if not preco or preco<=0:
            raise ValueError("O preço precisa ser um número maior que 0!")
        self._p=preco
    
    def getEstq(self):
        return self._e
    def setEstq(self,estoque):
        if estoque is None or estoque<0:
            raise ValueError("A quantidade no estoque não pode ser negativa!")
        self._e=estoque

    def getId_Cat(self):
        return self._id_cat
    def setId_Cat(self,id_categoria):
        if id_categoria is not None and id_categoria<0:
            raise ValueError("O ID da categoria não pode ser negativo!")
        self._id_cat=id_categoria
    
    def __str__(self):
        return f"ID: {self.getId()} | Descrição: {self.getDesc()} | Preço: {self.getPreco()} | Estoque: {self.getEstq()} | Categoria: {self.getId_Cat()}"
    
    def to_json(self):
        return {
            "id": self._id,
            "descricao": self._desc,
            "preco": self._p,
            "estoque": self._e,
            "id_categoria": self._id_cat
        }

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"],dic["descricao"], dic["preco"],dic["estoque"],dic.get("id_categoria",0))