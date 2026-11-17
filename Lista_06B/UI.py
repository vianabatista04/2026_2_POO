from Cliente import Cliente,Categoria,Produto
from DAO import ClienteDAO,CategoriaDAO,ProdutoDAO

class UI:
    @staticmethod
    def main():
        op=0
        while op !=13:
            op=UI.menu()
            if op == 1: UI.Cliente_Listar()
            elif op == 2: UI.Cliente_Inserir()
            elif op == 3: UI.Cliente_Atualizar()
            elif op == 4: UI.Cliente_Excluir()
            elif op == 5: UI.Categoria_Listar()
            elif op == 6: UI.Categoria_Inserir()
            elif op == 7: UI.Categoria_Atualizar()
            elif op == 8: UI.Categoria_Excluir()
            elif op == 9: UI.Produto_Listar()
            elif op == 10: UI.Produto_Inserir()
            elif op == 11: UI.Produto_Atualizar()
            elif op == 12: UI.Produto_Excluir()
            elif op == 13: print("Finalizando")
            else: 
                print("Opção Inválida! Escolha um valor de 1 até 13")
    
    @staticmethod
    def menu():
        print("1 - Listar Cliente, 2 - Inserir Cliente, 3 - Atualizar Cliente, 4 - Excluir Cliente, 5 - Listar Categoria, 6 - Inserir Categoria, 7 - Atualizar Categoria, 8 - Excluir Categoria , 9 - Listar Produtos, 10 - Inserir Produtos, 11 - Atualizar Produtos, 12 - Excluir Produtos , 13 - Fim ")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError: return 0
    
    @staticmethod
    def Cliente_Listar():
        print("==== Lista de Clientes ====")
        clientes=ClienteDAO.Listar()
        if not clientes:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)
    
    @staticmethod
    def Cliente_Inserir():
        print("==== Novo Cliente ====")
        try:
            id=int(input("ID: "))
            nome=input("Nome: ")
            email=input("Email: ")
            telefone=input("Telefone (com DDD, 11 dígitos): ")
            novo_cliente=Cliente(id,nome,email,telefone)
            ClienteDAO.Inserir(novo_cliente)
            print("Cliente cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Cliente_Atualizar():
        print("\n==== Atualizar Informação do Cliente ====")
        try:
            id_busca = int(input("Digite o ID para ser alterado: "))
            cliente_existente=ClienteDAO.Listar_id(id_busca)
            if cliente_existente is None:
                print("Cliente não encontrado com o ID informado!")
                return
            print("Informe os novos dados: ")
            nome=input("Nome: ")
            email=input("Email: ")
            telefone=input("Telefone (com DDD, 11 dígitos): ")
            atualizado=Cliente(id_busca,nome,email,telefone)
            ClienteDAO.Atualizar(atualizado)
            print("Cliente Atualizado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Cliente_Excluir(): 
        print("\n==== Excluir Cliente ====")
        try:
            id_busca = int(input("Digite o ID para ser excluído: "))
            cliente_existente=ClienteDAO.Listar_id(id_busca)
            if cliente_existente is None:
                print("Cliente não encontrado com o ID informado!")
                return
            ClienteDAO.Excluir(cliente_existente)
            print("Cliente Excluído!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!") 
    
    @staticmethod
    def Categoria_Listar():
        print("==== Lista de Categorias ====")
        categorias=CategoriaDAO.Listar()
        if not categorias:
            print("Nenhuma categoria cadastrada")
        else:
            for categoria in categorias:
                print(categoria)
    
    @staticmethod
    def Categoria_Inserir():
        print("==== Nova Categoria ====")
        try:
            id=int(input("ID: "))
            descricao=input("Descrição: ")
            nova_categoria=Categoria(id,descricao)
            CategoriaDAO.Inserir(nova_categoria)
            print("Categoria cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Categoria_Atualizar():
        print("\n==== Atualizar Informação da Categoria ====")
        try:
            id_busca = int(input("Digite o ID para ser alterado: "))
            categoria_existente=CategoriaDAO.Listar_id(id_busca)
            if categoria_existente is None:
                print("Categoria não encontrada com o ID informado!")
                return
            print("Informe os novos dados: ")
            descricao=input("Descrição: ")
            atualizado=Cliente(id_busca,descricao)
            CategoriaDAO.Atualizar(atualizado)
            print("Categoria Atualizada!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Categoria_Excluir(): 
        print("\n==== Excluir Categoria ====")
        try:
            id_busca = int(input("Digite o ID para ser excluído: "))
            categoria_existente=CategoriaDAO.Listar_id(id_busca)
            if categoria_existente is None:
                print("Categoria não encontrada com o ID informado!")
                return
            CategoriaDAO.Excluir(categoria_existente)
            print("Categoria Excluída!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!") 
    
    @staticmethod
    def Produto_Listar():
        print("==== Lista de Produtos ====")
        produtos=ProdutoDAO.Listar()
        if not produtos:
            print("Nenhum produto cadastrado")
        else:
            for produto in produtos:
                print(produto)
    
    @staticmethod
    def Produto_Inserir():
        print("==== Novo Produto ====")
        try:
            id = int(input("ID: "))
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            UI.Categoria_Listar()
            id_categoria = int(input("ID da Categoria: "))
            novo_produto = Produto(id, descricao, preco, estoque, id_categoria)
            ProdutoDAO.Inserir(novo_produto)
            print("Produto cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Produto_Atualizar():
        print("\n==== Atualizar Informação do Produto ====")
        try:
            id_busca = int(input("Digite o ID do produto para ser alterado: "))
            produto_existente = ProdutoDAO.Listar_Id(id_busca)
            if produto_existente is None:
                print("Produto não encontrado com o ID informado!")
                return
            print("Informe os novos dados: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            UI.Categoria_Listar()
            id_categoria = int(input("ID da Categoria: "))
            atualizado = Produto(id_busca, descricao, preco, estoque, id_categoria)
            ProdutoDAO.Atualizar(atualizado)
            print("Produto Atualizado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Produto_Excluir(): 
        print("\n==== Excluir Produto ====")
        try:
            id_busca = int(input("Digite o ID do produto para ser excluído: "))
            produto_existente = ProdutoDAO.Listar_Id(id_busca)
            if produto_existente is None:
                print("Produto não encontrado com o ID informado!")
                return
            ProdutoDAO.Excluir(produto_existente)
            print("Produto Excluído!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!")
UI.main()