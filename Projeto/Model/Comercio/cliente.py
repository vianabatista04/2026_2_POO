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