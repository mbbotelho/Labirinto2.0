__author__ = 'Michelle'
import sqlite3


class DaoJogada:
    def __init__(self):
        try:
            self.conexao = sqlite3.connect('Jogo_labirinto.db')
        except sqlite3.Error:
            print("Error na conexao com o banco ",sqlite3.Error)

    def inciar_conexao(self):
        try:
            cur = self.conexao.cursor()
            cur.executescript("CREATE TABLE IF NOT EXISTS Jogada(Id_Nivel INTEGER, id_pessoa INTEGER, tempo INTEGER);")
            self.conexao.commit()

            #for linha in cur.fetchall():
             #   print(linha)
              #  self.conexao.commit()

        except sqlite3.Error:
            if self.conexao:
                self.conexao.rollback()

            print("Error : Na criacao do banco ",sqlite3.Error)

    def inserir_jogada(self,jogada):
        lista=[jogada.id_pessoa,jogada.id_nivel]
        print("lst_jogada",lista)
        try:
            cur = self.conexao.cursor()
            cur.execute("""SELECT * FROM Jogada WHERE id_pessoa = ? and id_nivel = ?""",lista)
            jogada_banco=cur.fetchone()
            lista=[jogada.tempo,jogada.id_pessoa,jogada.id_nivel]
            print("tempo,pessoa,nivel",lista)

            if jogada_banco !=None:
                if jogada.tempo < jogada_banco[2]:### refazer
                    print("entrei")
                    cur.execute(""" UPDATE Jogada SET tempo = ? WHERE id_pessoa = ? and id_nivel = ?""",lista)

            else:
                  cur.execute("INSERT INTO Jogada (tempo,id_pessoa,id_nivel) VALUES (?,?,?)",lista)

            cur.execute("SELECT * FROM Jogada")
            for linha in cur.fetchall():
                print("linha1",linha)
                self.conexao.commit()


        except sqlite3.IntegrityError:
            print("erro: inserir jogada")

    def retorna_jogadas_nivel(self,nome_nivel):
        try:
            print(nome_nivel)
            lista=[nome_nivel]
            lista_record=[]
            cur = self.conexao.cursor()
            cur.execute("""SELECT * FROM Jogada INNER JOIN nivel ON  nivel.Nome=? and jogada.Id_Nivel =nivel.Id_Nivel """,lista)
            self.conexao.commit()

            for linha in cur.fetchall():
                    print("linha",linha)
                    lista_record.append(linha)
                    self.conexao.commit()
            print(lista_record)
            return lista_record

        except sqlite3.Error as erro:
            print("Erro no banco de dados: ", erro)

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()




