from random import *


class CriarLabirinto(object):

    def __init__(self,larg,alt):
        self.largura=larg
        self.altura=alt
        self.lst_componentes=[]# representa uma lista de Componentes
        self.make_maze()

    def walk(self,x,y,vis,ver,hor):# cria labirinto
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for xx, yy in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            self.walk(xx,yy,vis,ver,hor)

    def make_maze(self): # cria o labirinto aleatorio
        vis = [[0] * self.largura + [1] for _ in range(self.altura)] + [[1] * (self.altura + 1)]
        ver = [["|  "] * self.largura + ['|'] for _ in range(self.altura)] + [[]]
        hor = [["+--"] * self.largura + ['+'] for _ in range(self.altura + 1)]

        self.walk(randrange(self.largura), randrange(self.altura),vis,ver,hor)
        lab=self.junta_lista(self,ver,hor)
        maze=[]
        maze=self.converte_labirinto(self,lab)
        self.lst_componentes = maze
        self.escolhe_fim_inicio()

    @staticmethod
    def junta_lista(self,ver,hor):# junta duas listas intercaladas
        lab = [hor[0],ver[0]]
        for i in range(1,len(hor)):
            lab.append(hor[i])
            lab.append(ver[i])
        return lab
    @staticmethod
    def converte_labirinto(self,lab):
        labirinto=[]
        for i in range(len(lab)):
            linha=[]
            for j in range(len(lab[i])):
                if lab[i][j] == '+' or lab[i][j]=="|":
                    linha.append("B")
                elif lab[i][j]=="+--" :
                    linha.append("B")
                    linha.append("B")
                elif lab[i][j]=="   ":
                     linha.append("M")
                     linha.append("M")
                elif lab[i][j] == "|  " or lab[i][j]=="+  ":
                    linha.append("B")
                    linha.append("M")
            labirinto.append(linha)

        return labirinto


    def desenha_labirinto(self,localizacao_x,localizacao_y):
       inicio=localizacao_x
       lst_blocos=[]
       lst_matos=[]
       lst_inicio_fim=[]
       for i in range(len(self.lst_componentes)):
          for j in range(len(self.lst_componentes[i])):
              if self.lst_componentes[i][j]=="B":
                 lst_blocos.append([localizacao_x,localizacao_y,30,30])
              elif self.lst_componentes[i][j]=="M":
                 lst_matos.append([localizacao_x,localizacao_y,30,30])
              elif self.lst_componentes[i][j]=="I":
                  self.coord_inicio=[localizacao_x,localizacao_y,30,30]
                  lst_matos.append(self.coord_inicio)
              elif self.lst_componentes[i][j]=="F" :
                  self.coord_fim=[localizacao_x,localizacao_y,30,30]
              localizacao_x+=30
          localizacao_x=inicio
          localizacao_y+=30
       lst_coordenadas=[lst_blocos,lst_matos,self.coord_inicio,self.coord_fim]
       return lst_coordenadas


    def gera_coordenada(self):
        linha=randint(0,len(self.lst_componentes)-2)
        coluna=randint(0,len(self.lst_componentes[0])-2)
        return linha,coluna

    def escolhe_fim_inicio(self):
        linha_inicio,coluna_inicio=self.gera_coordenada()
        while self.lst_componentes[linha_inicio][coluna_inicio]=="B":
            linha_inicio,coluna_inicio=self.gera_coordenada()
        self.lst_componentes[linha_inicio][coluna_inicio]='I'

        linha_final,coluna_final=self.gera_coordenada()

        while self.lst_componentes[linha_final][coluna_final]=="B" and coluna_final==coluna_inicio and linha_final==linha_inicio:
            linha_final,coluna_final=self.gera_coordenada()
        self.lst_componentes[linha_final][coluna_final]='F'
