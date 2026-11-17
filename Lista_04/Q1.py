class Musica:
    def __init__(self, titulo, artista, album):
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_titulo(self,titulo):
        if titulo == "": raise ValueError("Título deve ser informado")
        self.__titulo=titulo
    def set_artista(self,artista):
        if artista == "": raise ValueError("Artista deve ser informado")
        self.__artista=artista
    def set_album(self,album):
        if album == "": raise ValueError("Álbum deve ser informado")
        self.__album=album
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def __str__(self):
          return f"{self.get_titulo()} - {self.get_artista()} - {self.get_album()}"

class Playlist:
    def __init__(self, nome, descricao):
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.__musicas = []
    def set_nome(self,nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome=nome
    def set_descricao(self,descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self.__descricao=descricao
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def inserir(self, m):
        self.__musicas.append(m)
    def listar(self):
        return self.__musicas
    def __str__(self):
        return f"A playlist '{self.__nome}' ({self.__descricao}) tem {len(self.__musicas)} música(s)"   

class UI:
    playlists=[]
    @staticmethod
    def main():
        op=0
        while op!=5:
            op=UI.menu()
            if op==1: UI.inserir_playLists()
            if op==2: UI.listar_playLists()
            if op==3: UI.inserir_musica()
            if op==4: UI.listar_musicas()

    @staticmethod
    def menu():
        print("1 - Inserir PlayList, 2 - Listar PlayList,3 - Inserir Música, 4 - Listar Músicas, 5 - Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir_playLists(cls):
        nome=input("Informe o nome da playlist: ")
        desc=input("Informe a descrição: ")
        x=Playlist(nome,desc)
        cls.playlists.append(x)
        pass
    @classmethod
    def listar_playLists(cls):
        for x in cls.playlists: print(x)
    @classmethod
    def inserir_musica(cls):
        if len(cls.playlists)==0:
            print("Insira uma playlist antes de inserir as músicas!")
            return
        for i, x in enumerate(cls.playlists):
            print(i, " - ", x.get_nome())
        index=int(input("Informe o número da playlist: "))
        titulo=input("Informe o nome da música: ")
        artista=input("Informe o artista: ")
        album=input("Informe o álbum: ")
        m=Musica(titulo,artista,album)
        cls.playlists[index].inserir(m)
    @classmethod
    def listar_musicas(cls):
        for x in cls.playlists: 
            print("Playlist:",x.get_nome())
            for m in x.listar():
                print(" ",m)

UI.main()
