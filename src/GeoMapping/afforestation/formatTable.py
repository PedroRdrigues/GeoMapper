# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:37:01 2024

@author: PedroRdrigues
"""

from dataclasses import dataclass
from unidecode import unidecode


"""
Realizar formatação e padronização da tabela
"""


@dataclass
class FormatTable:
    df: None
    colunms: None

    def __post_init__(self):
        # Formata todas as colunas e renomeia as colunas respectivas de coordenadas x e y
        self.renameColumns()
        self.removeNone()  # Remove linhas e colunas totalmente vazias
        self.formatCoordColumns()  # Formata e transforma as coordenadas para decimal
        self.renameNone()  # Preenche dados vazios por "Desconhecido"

    def renameColumns(self):
        index = -1
        while True:
            if 'coordenada' not in self.colunms[index].lower() \
                    and 'coordenadas' not in self.colunms[index].lower():

                index -= 1
            else:
                break

        self.df = self.df.rename(
            columns={self.colunms[index-1]: 'coordenadas_x'})
        self.df = self.df.rename(
            columns={self.colunms[index]: 'coordenadas_y'})

        # Padronizar nomes de colunas
        self.df.columns = [unidecode(col.strip().lower().replace(
            " ", "_").replace(".", "")) for col in self.df.columns]

    def formatCoordColumns(self):
        s, e = 0, 0

        for i in range(len(self.df)):
            try:
                coods_X = str(self.df['coordenadas_x'][i]).replace("°", " ").replace(
                    "º", " ").replace("'", " ").replace('"', ' ').replace(",", ".").split()

                if len(coods_X) < 4:
                    coods_X.append('S')

                grausX = float(coods_X[0])
                minutosX = float(coods_X[1].replace("'", ""))
                segundosX = float(coods_X[2].replace("'", ""))
                hemisferioX = coods_X[3]
                self.df.loc[i, "coordenadas_x"] = self.dmsToDecimal(
                    grausX, minutosX, segundosX, hemisferioX)
                s += 1

            except Exception as err:
                self.df.loc[i, "coordenadas_x"] = None
                print(f"\tErro X - {i+2} : ", err)
                e += 1

            try:
                coods_Y = str(self.df['coordenadas_y'][i]).replace("°", " ").replace(
                    "º", " ").replace("'", " ").replace('"', ' ').replace(",", ".").split()

                if len(coods_Y) < 4:
                    coods_Y.append('W')
                grausY = float(coods_Y[0])
                minutosY = float(coods_Y[1].replace("'", ""))
                segundosY = float(coods_Y[2].replace("'", ""))
                hemisferioY = coods_Y[3]
                self.df.loc[i, "coordenadas_y"] = self.dmsToDecimal(
                    grausY, minutosY, segundosY, hemisferioY)
                s += 1

            except Exception as err:
                self.df.loc[i, "coordenadas_y"] = None
                print(f"\tErro Y - {i+2} : ", err)
                e += 1

        print("\nConversão de coordenadas -> Sucessos: ", s)
        print("\nConversão de coordenadas -> Erros: ", e)

    def dmsToDecimal(self, graus, minutos, segundos, hemisferio):
        hemisferio = hemisferio.upper()
        h = 1

        if hemisferio == 'O' or hemisferio == 'S' or hemisferio == 'W':
            h = -1
        decimal = (graus + minutos / 60 + segundos / 3600) * h

        return decimal

    def removeNone(self):
        for col in self.df:
            for i, v in enumerate(self.df[col]):
                if v == '-':
                    self.df.loc[i, col] = None

        # Remover colunas totalmente vazias
        self.df.dropna(axis=1, how="all", inplace=True)

        # Remover linhas totalmente vazias
        self.df.dropna(axis=0, how="all", inplace=True)

    def renameNone(self):
        self.df.fillna("Desconhecido", inplace=True)
