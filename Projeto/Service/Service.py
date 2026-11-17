from Model.Comercio.cliente import Cliente
from Model.Comercio.categoria import Categoria
from Model.Comercio.produto import Produto
from Model.DAO.clienteDAO import ClienteDAO
from Model.DAO.categoriaDAO import CategoriaDAO
from Model.DAO.produtoDAO import ProdutoDAO

class Service:
    @staticmethod
    def Cliente_Inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO.Inserir(c)

    @staticmethod
    def Cliente_Listar():
        return ClienteDAO.Listar()

    @staticmethod
    def Cliente_Listar_id(id):
        return ClienteDAO.Listar_id(id)

    @staticmethod
    def Cliente_Atualizar(id,nome,email,fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.Atualizar(c)

    @staticmethod
    def Cliente_Excluir(id):
        c = Cliente(id, "", "", "")
        ClienteDAO.Excluir(c)

    @staticmethod
    def Categoria_Inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO.Inserir(c)

    @staticmethod
    def Categoria_Listar():
        return CategoriaDAO.Listar()

    @staticmethod
    def Categoria_Listar_id(id):
        return CategoriaDAO.Listar_id(id)

    @staticmethod
    def Categoria_Atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.Atualizar(c)

    @staticmethod
    def Categoria_Excluir(id):
        c = Categoria(id, "")
        CategoriaDAO.Excluir(c)

    @staticmethod
    def Produto_Inserir(descricao, preco, estoque, idCategoria):
        p = Produto(0, descricao, preco, estoque, idCategoria)
        ProdutoDAO.Inserir(p)

    @staticmethod
    def Produto_Listar():
        return ProdutoDAO.Listar()

    @staticmethod
    def Produto_Listar_id(id):
        return ProdutoDAO.Listar_id(id)

    @staticmethod
    def Produto_Atualizar(id,descricao,preco,estoque,idCategoria):
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.Atualizar(p)

    @staticmethod
    def Produto_Excluir(id):
        p = Produto(id, "", 0.0, 0, 0)
        ProdutoDAO.Excluir(p)

    @staticmethod
    def Produto_Reajustar(percentual):
        for p in ProdutoDAO.Listar():
            novo_preco = p.get_preco() * (1 + percentual / 100)
            p.set_preco(novo_preco)
            ProdutoDAO.Atualizar(p)