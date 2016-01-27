__author__ = 'Michelle'
from cgd.DaoPessoa import *
from cdp.Pessoa import *

class AplGerenciarPessoa:

    def Cadastrar_pessoa(self,dados_pessoa):
        dados=[]
        for i in range(len(dados_pessoa)):
            if dados_pessoa[i]=='':
                dados.append(None)
            else:
                dados.append(dados_pessoa[i])

        dao_pessoa = DaoPessoa()
        dao_pessoa.iniciar_conexao()
        erro=dao_pessoa.insere_pessoa(dados)
        dao_pessoa.fechar_conexao()
        return erro

    def login_pessoa(self,login_senha):
        print(login_senha)
        ID,NOME=0,1

        dao_pessoa = DaoPessoa()

        dao_pessoa = DaoPessoa()
        dao_pessoa.iniciar_conexao()
        pessoa_banco=dao_pessoa.logar_pessoa(login_senha)
        dao_pessoa.fechar_conexao()
        print(pessoa_banco)
        if pessoa_banco !=None:
            pessoa=Pessoa(pessoa_banco[ID],pessoa_banco[NOME])
            print(pessoa.id,pessoa.nome)
            return pessoa
        else:
            return pessoa_banco


    def salvar_labirinto(self,id_pessoa,labirinto):
        dao_pessoa = DaoPessoa()
        dao_pessoa.iniciar_conexao()
        dao_pessoa.salvar_labirinto(id_pessoa,labirinto)
        dao_pessoa.fechar_conexao()

    def retorna_nome(self,id_pessoa):
        dao_pessoa = DaoPessoa()
        nome=dao_pessoa.retorna_nome(id_pessoa)
        dao_pessoa.fechar_conexao()
        return nome













