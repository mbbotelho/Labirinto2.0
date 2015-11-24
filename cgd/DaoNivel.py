__author__ = 'Michelle'

import sqlite3

class DaoNivel:
    def __init__(self):
        try:
            self.conexao = sqlite3.connect('Jogo_labirinto.db')
        except sqlite3.Error:
            print("Error na conexao com o banco " ,sqlite3.Error)

    def iniciar_conexao(self):
        try:
            cur = self.conexao.cursor()
            cur.executescript("CREATE TABLE IF NOT EXISTS Nivel(Id_Nivel INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT UNIQUE);")
            self.conexao.commit()
            self.inserir_niveis()

        except sqlite3.Error:
            if self.conexao:
                self.conexao.rollback()

            print("Error : Na criacao do banco ")

    def inserir_niveis(self):
       try:
            cur = self.conexao.cursor()
            cur.execute("INSERT INTO Nivel (Nome) VALUES ('Facil')")
            cur.execute("INSERT INTO Nivel (Nome) VALUES ('Medio')")
            cur.execute("INSERT INTO Nivel (Nome) VALUES ('Dificil')")
            cur.execute("SELECT * FROM Nivel")

            for linha in cur.fetchall():
                print(linha)
                self.conexao.commit()

       except sqlite3.IntegrityError:
            print("erro: ja existe esse nivel")

    def retorna_id(self,nome):
        try:
            c = self.conexao.cursor()
            c.execute("""SELECT * FROM nivel WHERE nome = ?""",[nome])
            id_nivel = c.fetchone()
            return id_nivel[0]

        except sqlite3.Error:
            print("Erro ao acessar o banco")

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()