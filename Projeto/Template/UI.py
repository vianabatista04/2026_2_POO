from Service.Service import Service

class UI:
    @staticmethod
    def main():
        op=0
        while op !=14:
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
            elif op == 13: UI.Produto_Reajustar()
            elif op == 14: print("Finalizando!")
            else: 
                print("Opção Inválida! Escolha um valor de 1 até 13")
    
    @staticmethod
    def menu():
        print("1 - Listar Cliente, 2 - Inserir Cliente, 3 - Atualizar Cliente, 4 - Excluir Cliente, 5 - Listar Categoria, 6 - Inserir Categoria, 7 - Atualizar Categoria, 8 - Excluir Categoria , 9 - Listar Produtos, 10 - Inserir Produtos, 11 - Atualizar Produtos, 12 - Excluir Produtos , 13 - Reajustar Produto ")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError: return 0
    
    @staticmethod
    def Cliente_Listar():
        print("==== Lista de Clientes ====")
        clientes = Service.Cliente_Listar()
        if not clientes:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)
    
    @staticmethod
    def Cliente_Inserir():
        print("==== Novo Cliente ====")
        try:
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone (com DDD, 11 dígitos): ")
            Service.Cliente_Inserir(nome, email, telefone)
            print("Cliente cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Cliente_Atualizar():
        print("\n==== Atualizar Informação do Cliente ====")
        try:
            id_busca = int(input("Digite o ID para ser alterado: "))
            if Service.Cliente_Listar_id(id_busca) is None:
                print("Cliente não encontrado com o ID informado!")
                return
            print("Informe os novos dados: ")
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone (com DDD, 11 dígitos): ")
            Service.Cliente_Atualizar(id_busca, nome, email, telefone)
            print("Cliente Atualizado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Cliente_Excluir(): 
        print("\n==== Excluir Cliente ====")
        try:
            id_busca = int(input("Digite o ID para ser excluído: "))
            if Service.Cliente_Listar_id(id_busca) is None:
                print("Cliente não encontrado com o ID informado!")
                return
            Service.Cliente_Excluir(id_busca)
            print("Cliente Excluído!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!")

    @staticmethod    
    def Categoria_Listar():
        print("==== Lista de Categorias ====")
        categorias = Service.Categoria_Listar()
        if not categorias:
            print("Nenhuma categoria cadastrada")
        else:
            for categoria in categorias:
                print(categoria)
    
    @staticmethod
    def Categoria_Inserir():
        print("==== Nova Categoria ====")
        try:
            descricao = input("Descrição: ")
            Service.Categoria_Inserir(descricao)
            print("Categoria cadastrada!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Categoria_Atualizar():
        print("\n==== Atualizar Informação da Categoria ====")
        try:
            id_busca = int(input("Digite o ID para ser alterado: "))
            if Service.Categoria_Listar_id(id_busca) is None:
                print("Categoria não encontrada com o ID informado!")
                return
            print("Informe os novos dados: ")
            descricao = input("Descrição: ")
            Service.Categoria_Atualizar(id_busca, descricao)
            print("Categoria Atualizada!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Categoria_Excluir(): 
        print("\n==== Excluir Categoria ====")
        try:
            id_busca = int(input("Digite o ID para ser excluído: "))
            if Service.Categoria_Listar_id(id_busca) is None:
                print("Categoria não encontrada com o ID informado!")
                return
            Service.Categoria_Excluir(id_busca)
            print("Categoria Excluída!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!")
    
    @staticmethod
    def Produto_Listar():
        print("==== Lista de Produtos ====")
        produtos = Service.Produto_Listar()
        if not produtos:
            print("Nenhum produto cadastrado")
        else:
            for produto in produtos:
                print(produto)
    
    @staticmethod
    def Produto_Inserir():
        print("==== Novo Produto ====")
        try:
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            UI.Categoria_Listar()
            id_categoria = int(input("ID da Categoria: "))
            Service.Produto_Inserir(descricao, preco, estoque, id_categoria)
            print("Produto cadastrado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Produto_Atualizar():
        print("\n==== Atualizar Informação do Produto ====")
        try:
            id_busca = int(input("Digite o ID do produto para ser alterado: "))
            if Service.Produto_Listar_id(id_busca) is None:
                print("Produto não encontrado com o ID informado!")
                return
            print("Informe os novos dados: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            UI.Categoria_Listar()
            id_categoria = int(input("ID da Categoria: "))
            Service.Produto_Atualizar(id_busca, descricao, preco, estoque, id_categoria)
            print("Produto Atualizado!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
    
    @staticmethod
    def Produto_Excluir(): 
        print("\n==== Excluir Produto ====")
        try:
            id_busca = int(input("Digite o ID do produto para ser excluído: "))
            if Service.Produto_Listar_id(id_busca) is None:
                print("Produto não encontrado com o ID informado!")
                return
            Service.Produto_Excluir(id_busca)
            print("Produto Excluído!")
        except ValueError:
            print("Erro de validação!: O ID precisa ser um número inteiro!")

    @staticmethod
    def Produto_Reajustar():
        print("\n==== Reajustar Preço dos Produtos ====")
        try:
            percentual = float(input("Informe o percentual de reajuste (ex: 10 ou -10): "))
            Service.Produto_Reajustar(percentual)
            print("Preços reajustados!")
        except ValueError as e:
            print(f"Problema de validação!: {e}")
UI.main()