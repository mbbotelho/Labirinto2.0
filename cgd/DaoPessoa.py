__author__ = 'Michelle'

import sqlite3
class DaoPessoa():
    def __init__(self):
        try:
            self.conexao = sqlite3.connect('Jogo_labirinto.db')
        except sqlite3.Error as e:
            print("Error na conexao com o banco ",sqlite3.Error)

    def iniciar_conexao(self):
        try:
            cur = self.conexao.cursor()
            cur.executescript("CREATE TABLE IF NOT EXISTS Pessoa(Id_Pessoa INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL,Login TEXT UNIQUE NOT NULL, Senha TEXT NOT NULL, Data_nascimento TEXT,email TEXT,Labirinto_salvo TEXT );")
            self.conexao.commit()

        except sqlite3.Error:
            if self.conexao:
                self.conexao.rollback()
            print("Error : Na criacao do banco ",sqlite3.Error)

    def insere_pessoa(self,pessoa):
        print(pessoa)
        try:
            cur = self.conexao.cursor()
            cur.execute("INSERT INTO Pessoa (Nome,login,senha,data_nascimento,email) VALUES (?,?,?,?,?)",pessoa)
            self.conexao.commit()
            cur.execute("SELECT * FROM pessoa")

            for linha in cur.fetchall():
                print(linha)
                self.conexao.commit()
            return True

        except sqlite3.IntegrityError:
            print("erro: ja existe esse login")
            return False

    def logar_pessoa(self,login_senha):
        try:
            print(login_senha)
            c=self.conexao.cursor()
            c.execute("""SELECT * FROM pessoa WHERE login = ? and senha = ?""",login_senha)
            pessoa=c.fetchone()
            print(pessoa)


            if pessoa == None:
                if self.conexao:
                    self.conexao.close()

                print("Login ou senha errado")
            return pessoa

        except sqlite3.Error:
            print("Erro no banco de dados")

    def salvar_labirinto(self,id_pessoa,labirinto):
        lista=[labirinto,id_pessoa]
        print(lista)
        c=self.conexao.cursor()
        c.execute(""" UPDATE Pessoa SET labirinto_salvo = ? WHERE id_pessoa = ?""",lista)

    def retorna_nome(self,id_pessoa):
        try:
            c=self.conexao.cursor()
            c.execute("""SELECT * FROM pessoa WHERE id_pessoa=?""",[id_pessoa])
            pessoa=c.fetchone()
            print(pessoa)

            if pessoa != None:
                return pessoa[1]

        except sqlite3.Error:
            print("Erro no banco de dados")

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()





