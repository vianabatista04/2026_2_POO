from datetime import datetime, timedelta

class Musica:
    def __init__(self,id, titulo, artista, album,duracao):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
        self.set_duracao(duracao)

    def set_id(self,id):
        if id is None or id<=0: raise ValueError("O ID precisa ser um número maior que zero!")
        self.__id=id
    def set_titulo(self,titulo):
        if not titulo or not titulo.strip(): raise ValueError("Título deve ser informado")
        self.__titulo=titulo.strip()
    def set_artista(self,artista):
        if not artista or not artista.strip(): raise ValueError("Artista deve ser informado")
        self.__artista=artista.strip()
    def set_album(self,album):
        if not album or not album.strip(): raise ValueError("Álbum deve ser informado")
        self.__album=album.strip()
    def set_duracao(self,duracao):
        if not duracao or duracao.total_seconds()<=0: raise ValueError("Duração deve ser positiva")
        self.__duracao=duracao

    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def get_duracao(self): return self.__duracao

    def __str__(self):
          return f"Música {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} | Duração: {self.__duracao}"

class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
    
    def set_id(self,id):
        if id is None or id<=0: raise ValueError("O ID precisa ser um número maior que zero!")
        self.__id=id
    def set_nome(self,nome):
        if not nome or nome.strip() == "": raise ValueError("Nome deve ser informado")
        self.__nome=nome.strip()
    def set_descricao(self,descricao):
        if descricao is None or not descricao.strip(): raise ValueError("Descrição deve ser informada")
        self.__descricao=descricao.strip()

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao

    def tempo_total(self,lista_itens, lista_musicas):
        tempo=timedelta()
        for item in lista_itens:
            if item.get_id_playlist()==self.__id:
                for musica in lista_musicas:
                    if musica.get_id()==item.get_id_musica():
                        tempo+=musica.get_duracao()
                        break
        return tempo

    def __str__(self):
        return f"Playlist {self.__id} | Nome: '{self.__nome}'| Descrição: {self.__descricao}"   

class PlayListItem:
    def __init__(self,id, id_playlist, id_musica, data_inclusao,sequencia):
        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_musica(id_musica)
        self.set_data_inclusao(data_inclusao)
        self.set_sequencia(sequencia)
    
    def set_id(self,id):
        if id is None or id<=0: raise ValueError("O ID precisa ser um número maior que zero!")
        self.__id=id

    def set_id_playlist(self,id_playlist):
        if id_playlist is None or id_playlist<=0: raise ValueError("O ID da playlist precisa ser um número maior que zero")
        self.__id_playlist=id_playlist

    def set_id_musica(self,id_musica):
        if id_musica is None or id_musica<=0: raise ValueError("O ID da música precisa ser um número maior que zero")
        self.__id_musica=id_musica

    def set_data_inclusao(self,data_inclusao):
        if not data_inclusao :raise ValueError("A data não pode ser vazia!")
        self.__data_inclusao=data_inclusao

    def set_sequencia(self,sequencia):
        if sequencia is None or sequencia<=0: raise ValueError("O valor da sequência tem que ser maior que zero")
        self.__sequencia=sequencia

    def get_id(self): return self.__id
    def get_id_playlist(self): return self.__id_playlist
    def get_id_musica(self): return self.__id_musica
    def get_data_inclusao(self): return self.__data_inclusao
    def get_sequencia(self): return self.__sequencia

    def __str__(self):
        data_corrigida= self.__data_inclusao.strftime("%d/%m/%Y")
        return f"Item {self.__id} | Playlist ID: {self.__id_playlist} | Música ID: {self.__id_musica} | Adicionado em : {data_corrigida} | Sequência: {self.__sequencia}"
    
class UI:
    playlists=[]
    musicas=[]
    itens=[]

    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            elif op == 2: UI.listar_playlists()
            elif op == 3: UI.atualizar_playlist()
            elif op == 4: UI.excluir_playlist()
            elif op == 5: UI.inserir_musica()
            elif op == 6: UI.listar_musicas()
            elif op == 7: UI.atualizar_musica()
            elif op == 8: UI.excluir_musica()
            elif op == 9: UI.inserir_item()
            elif op == 10: UI.listar_itens()
            elif op == 11: UI.atualizar_item()
            elif op == 12: UI.excluir_item()
            elif op == 13: print("Finalizando")
            else: print("Opção Inválida! Escolha um valor de 1 até 13")

    @staticmethod
    def menu():
        print("\n==== MENU ====")
        print("1 - Inserir Playlist | 2 - Listar Playlists | 3 - Atualizar Playlist | 4 - Excluir Playlist")
        print("5 - Inserir Música   | 6 - Listar Músicas   | 7 - Atualizar Música   | 8 - Excluir Música")
        print("9 - Inserir Item     | 10 - Listar Itens    | 11 - Atualizar Item    | 12 - Excluir Item")
        print("13 - Fim")
        try:
            return int(input("Opção: "))
        except ValueError:
            return 0

    @staticmethod
    def inserir_playlist():
        print("\n==== Nova Playlist ====")
        try:
            id=int(input("ID: "))
            for pl in UI.playlists:
                if pl.get_id()==id:
                    print("Já tem uma playlist com esse ID")
                    return
            nome = input("Nome: ")
            desc = input("Descrição: ")
            nova=Playlist(id,nome,desc)
            UI.playlists.append(nova)
            print("Playlist criada!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")

    @staticmethod
    def listar_playlists():
        print("\n==== Lista de Playlists ====")
        if not UI.playlists:
            print("Nenhuma playlist cadastrada.")
            return
        for pl in UI.playlists:
            print(pl)
            tempo = pl.tempo_total(UI.itens, UI.musicas)
            print(f"Tempo Total: {tempo}")

    @staticmethod
    def atualizar_playlist():
        print("\n==== Atualizar Playlists ====")
        try:
            id_busca = int(input("Digite o ID que vai ser mudado: "))
            for pl in UI.playlists:
                if pl.get_id()==id_busca:
                    print("Digite os novos dados:")
                    novo_nome=input("Novo nome: ")
                    nova_desc=input("Nova descrição: ")
                    pl.set_nome(novo_nome)
                    pl.set_descricao(nova_desc)
                    print("Playlist atualizada!")
                    return
            print("Playlist não encontrada com esse ID")
        except ValueError as e:
            print(f"Problema de validação! {e}")

    @staticmethod
    def excluir_playlist():
        print("\n==== Excluir Playlists ====")
        try:
            id_busca = int(input("Digite o ID que vai ser excluído: "))
            for pl in UI.playlists:
                if pl.get_id()==id_busca:
                    UI.playlists.remove(pl)
                    UI.itens=[item for item in UI.itens if item.get_id_playlist() != id_busca]
                    print("Playlist excluída!")
                    return
            print("Playlist não encontrada com esse ID")
        except ValueError as e:
            print(f"Problema de validação! {e}")    
       
    @staticmethod
    def inserir_musica():
        print("\n==== Nova Música ====")
        try:
            id=int(input("ID: "))
            for m in UI.musicas:
                if m.get_id()==id:
                    print("Já tem uma música com esse ID")
                    return
            titulo = input("Título: ")
            artista = input("Artista: ")
            album = input("Álbum: ")
            minutos = int(input("Minutos: "))
            segundos = int(input("Segundos: "))
            duracao=timedelta(minutes=minutos, seconds=segundos)
            nova=Musica(id,titulo, artista, album, duracao)
            UI.musicas.append(nova)
            print("Música adicionada!")
        except ValueError as e:
            print(f"Problema de validação! {e}")

    @staticmethod
    def listar_musicas():
        print("\n==== Listar Músicas ====")
        if not UI.musicas:
            print("Nenhuma música cadastrada.")
            return
        for musica in UI.musicas:
            print(musica)

    @staticmethod
    def atualizar_musica():
        print("\n==== Atualizar Músicas ====")
        try:
            id_busca = int(input("Digite o ID que vai ser mudado: "))
            for m in UI.musicas:
                if m.get_id()==id_busca:
                    print("Digite os novos dados:")
                    novo_titulo=input("Novo título: ")
                    novo_artista=input("Novo artista: ")
                    novo_album=input("Novo álbum: ")
                    minutos=int(input("Minutos: "))
                    segundos = int(input("Segundos: "))
                    nova_duracao=timedelta(minutes=minutos, seconds=segundos)
                    m.set_titulo(novo_titulo)
                    m.set_artista(novo_artista)
                    m.set_album(novo_album)
                    m.set_duracao(nova_duracao)
                    print("Música atualizada!")
                    return
            print("Música não encontrada com esse ID")
        except ValueError as e:
            print(f"Problema de validação! {e}")

    @staticmethod
    def excluir_musica():
        print("\n==== Excluir Música ====")
        try:
            id_busca = int(input("Digite o ID que vai ser excluído: "))
            for m in UI.musicas:
                if m.get_id()==id_busca:
                    UI.musicas.remove(m)
                    UI.itens=[item for item in UI.itens if item.get_id_musica() != id_busca]
                    print("Música excluída!")
                    return
            print("Música não encontrada com esse ID")
        except ValueError as e:
            print(f"Problema de validação! {e}")    

    @staticmethod
    def inserir_item():
        print("\n==== Adicionar Música na Playlist ====")
        try:
            id=int(input("ID: "))
            for item in UI.itens:
                if item.get_id()==id:
                    print("Já tem um item com esse ID")
                    return
            id_playlist=int(input("ID da playlist: "))
            playlist_existe=False
            for pl in UI.playlists:
                if pl.get_id()==id_playlist:
                    playlist_existe=True
                    break
            if not playlist_existe:
                print("Playlist não encontrada!")
                return
            id_musica=int(input("ID da música: "))
            musica_existe=False
            for m in UI.musicas:
                if m.get_id()==id_musica:
                    musica_existe=True
                    break
            if not musica_existe:
                print("Música não encontrada!")
                return
            sequencia=int(input("Ordem da playlist: "))
            data_inclusao=datetime.now()
            novo_item=PlayListItem(id, id_playlist, id_musica,data_inclusao,sequencia)
            UI.itens.append(novo_item)
            print("Item adicionado na playlist!")
        except ValueError as e:
            print(f"Problema na validação!: {e}")
        
    @staticmethod
    def listar_itens():
        print("\n==== Listar Conteúdo das Playlists ====")
        if not UI.playlists:
            print("Nenhuma playlist cadastrada.")
            return
        for pl in UI.playlists:
            print(f"Playlist: {pl.get_id()} - {pl.get_nome()}")
            itens=False
            for item in UI.itens:
                if item.get_id_playlist()==pl.get_id():
                    itens=True
                    print(item)
            if not itens:
                print("Sem músicas cadastradas nesta playlist!")

    @staticmethod
    def atualizar_item():
        print("\n==== Atualizar Item da Playlists ====")
        try:
            id_busca = int(input("Digite o ID que vai ser mudado: "))
            for item in UI.itens:
                if item.get_id()==id_busca:
                    nova_seq=int(input("Nova Sequência: "))
                    item.set_sequencia(nova_seq)
                    print("Item modificado!")
                    return
            print("Item não encontrada com esse ID")
        except ValueError as e:
            print(f"Problema na validação! {e}")

    @staticmethod
    def excluir_item():
        print("\n==== Excluir Item ====")
        try:
            id_busca = int(input("Digite o ID do item que vai ser excluído: "))
            for item in UI.itens:
                if item.get_id()==id_busca:
                    UI.itens.remove(item)
                    print("Item removido!")
                    return
            print("Item não encontrado!")
        except ValueError as e:
            print(f"Problema na validação! {e}")    

if __name__ == "__main__":
    UI.main()