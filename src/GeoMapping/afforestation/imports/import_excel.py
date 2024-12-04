# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:14:38 2024

@author: PedroRdrigues
"""

from dataclasses import dataclass
import pandas as pd
from GeoMapping.afforestation import FormatTable

"""Importa a tabela em .csv e chama a função de formatação de tabela"""


@dataclass
class ImportExcel:
    filename: str
    path: str
    extension:str

    def __post_init__(self):
        self.df = pd.read_excel(f'{self.path}/{self.filename}{self.extension}')
        self.colunms = self.df.columns.tolist()
        self.formatTable()
    
    
    def formatTable(self):
        print(f'\n\n{self.filename}: ')
        self.df = FormatTable(self.df, self.colunms).df
        
        return self.df