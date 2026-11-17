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