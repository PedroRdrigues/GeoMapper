# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:20:42 2024

@author: PedroRdrigues
"""

from dataclasses import dataclass
import pandas as pd
from MapeAR.afforestation import FormatTable

"""Importa a tabela em .csv e chama a função de formatação de tabela"""


@dataclass
class ImportCsv:
    filename: str
    path: str
    

    def __post_init__(self):
        self.df = pd.read_csv(f'{self.path}/{self.filename}.csv',
                              encoding='ISO-8859-1', delimiter=';')
        self.colunms = self.df.columns.tolist()
        self.formatTable()
    
    
    def formatTable(self):
        print(f'\n\n{self.filename}: ')
        self.df = FormatTable(self.df, self.colunms).df
        
        return self.df

    

    

















 