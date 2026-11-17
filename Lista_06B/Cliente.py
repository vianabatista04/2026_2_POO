import json
import datetime

class Cliente:
    def __init__(self,id,nome,email,fone):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setFone(fone)
        
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
        if not fone or len(fone) != 11: 
            raise ValueError("Telefone precisa ser informado e com DDD e dígito nove na frente")
        self._fone=fone
    
    def __str__(self):
        return f"ID: {self.getId()} | Nome: {self.getNome()} | Email: {self.getEmail()} | Fone: {self.getFone()} "
    
    def to_json(self):
        return {
            "id": self._id,
            "nome": self._nome,
            "email": self._email,
            "fone": self._fone
        }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"],dic["nome"], dic["email"],dic["fone"])

class Categoria:
    def __init__(self,id,descricao):
        self.setId(id)
        self.setDesc(descricao)

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

    def __str__(self):
        return f"ID: {self.getId()} | Descrição: {self.getDesc()} "
    
    def to_json(self):
        return {
            "id": self._id, 
            "descricao": self._desc
            }

    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"],dic["descricao"])

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

class Venda:
    def __init__(self,id,data=None,carrinho=True,total=0.0,id_cliente=0):
        self.setId(id)
        if data is None: 
            data=datetime.datetime.now().strftime("%d/%m/%Y")
        self.setD(data)
        self.setC(carrinho)
        self.setT(total)
        self.setId_C(id_cliente)
        
    def getId(self):
        return self._id
    def setId(self,id):
        if not id or id<=0:
            raise ValueError("O ID precisa ser um número maior que 0!")
        self._id=id
    
    def getD(self):
        return self._d
    def setD(self,data):
        if not data:
            raise ValueError("A data não pode ser vazia!")
        if isinstance(data,datetime.datetime):
            self._d=data
        else:
            try:
                self._d=datetime.datetime.strptime(data,"%d/%m/%Y")
            except(ValueError,TypeError):
                raise ValueError("Data Inválida! Digite no formato DD/MM/AAAA")

    def getC(self):
        return self._c
    def setC(self,carrinho):
        if not isinstance(carrinho,bool):
            raise ValueError("O carrinho precisa ser True ou False!")
        self._c=carrinho
    
    def getT(self):
        return self._t
    def setT(self,total):
        if total is None or total<0:
            raise ValueError("O total não pode ser menor que 0!")
        self._t=total

    def getId_C(self):
        return self._id_c
    def setId_C(self,id_cliente):
        if id_cliente is not None and id_cliente<0:
            raise ValueError("O ID do cliente não pode ser negativo!")
        self._id_c=id_cliente
    
    def __str__(self):
        data_f=self.getD().strftime("%d/%m/%Y") if self.getD() else ""
        return f"ID: {self.getId()} | Data: {data_f} | Carrinho: {self.getC()} | Total: {self.getT()} | Cliente: {self.getId_C()}"
    
    def to_json(self):
        return {
            "id": self._id,
            "data": self._d.strftime("%d/%m/%Y") if self._d else None,
            "carrinho": self._c,
            "total": self._t,
            "id_cliente": self._id_c
        }

    @staticmethod
    def from_json(dic):
        v=Venda(dic["id"])
        v.setD(dic["data"])
        v.setC(dic["carrinho"])
        v.setT(dic["total"])
        v.setId_C(dic.get("id_cliente",0))
        return v