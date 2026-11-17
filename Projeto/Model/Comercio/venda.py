import datetime

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