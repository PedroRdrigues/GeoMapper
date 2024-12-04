# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:43:04 2024

@author: PedroRdrigues
"""
import os
from dataclasses import dataclass
from GeoMapping.afforestation import Afforestation


@dataclass
class FormatSpreadSheet:
    dataOrigin:str
    
    
    def __post_init__(self):
        p, ex = os.path.splitext(self.dataOrigin) # Separa a extensão do arquivo do restante da str
        listP = p.split('/') # Separa o restante da str em uma lista
        
        self.filename = listP[-1]
        self.path = '/'.join(listP[:-1])
        self.extension = ex
    
    # Metodo que define o objetivo da planilha e importa para onde será feita o reconhecimento do tipo de arquivo
    def afforestation(self):
        self.df = Afforestation(self.filename, self.path, self.extension).df
        
    
    # Vai receber o objeto/DataFrame criado e formatado, o caminho e o nome do arquivo que será salvo.
    def save(self, filename:str):
        path = 'Data'
        if not os.path.exists(path):
            os.mkdir(path)
        
        self.df.to_excel(f'{path}/{filename}.xlsx', index=False)
        
                
