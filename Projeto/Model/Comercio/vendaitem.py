class VendaItem:
    def __init__(self,id,qtd,preco,id_venda=0,id_produto=0):
        self.setId(id)
        self.setQtd(qtd)
        self.setPreco(preco)
        self.setId_V(id_venda)
        self.setId_P(id_produto)
        
    def getId(self):
        return self._id
    def setId(self,id):
        if not id or id<=0:
            raise ValueError("O ID precisa ser maior que 0!")
        self._id=id
    
    def getQtd(self):
        return self._qtd
    def setQtd(self,qtd):
        if not qtd or qtd<=0:
            raise ValueError("A quantidade precisa ser maior que 0!")
        self._qtd=qtd

    def getPreco(self):
        return self._p
    def setPreco(self,preco):
        if not preco or preco<=0:
            raise ValueError("O preço não pode ser menor ou igual a 0!")
        self._p=preco
    
    def getId_V(self):
        return self._id_v
    def setId_V(self,id_venda):
        if id_venda is not None and id_venda<0:
            raise ValueError("O ID da venda não pode ser negativo!")
        self._id_v=id_venda

    def getId_P(self):
        return self._id_p
    def setId_P(self,id_produto):
        if id_produto is not None and id_produto<0:
            raise ValueError("O ID do produto não pode ser negativo!")
        self._id_p=id_produto
    
    def __str__(self):
        return f"ID: {self.getId()} | Quantidade: {self.getQtd()} | Preço: {self.getPreco()} | Venda: {self.getId_V()} | Produto: {self.getId_P()}"
    
    def to_json(self):
        return {
            "id": self._id,
            "qtd": self._qtd,
            "preco": self._p,
            "id_venda": self._id_v,
            "id_produto": self._id_p
        }

    @staticmethod
    def from_json(dic):
        vi=VendaItem(dic["id"],dic["qtd"], dic["preco"])
        vi.setId_V(dic.get("id_venda",0))
        vi.setId_P(dic.get("id_produto",0))
        return vi