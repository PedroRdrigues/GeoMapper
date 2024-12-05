# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:43:04 2024

@author: PedroRdrigues
"""
import os
from dataclasses import dataclass
from GeoMapping.format import Reader


@dataclass
class FormatSpreadSheet:
    dataOrigin:str
    
    
    def __post_init__(self):
        p, ex = os.path.splitext(self.dataOrigin) # Separa a extensão do arquivo do restante da str
        listP = p.split('/') # Separa o restante da str em uma lista
        
        filename = listP[-1]
        path = '/'.join(listP[:-1])
        extension = ex
        
        self.df = Reader(filename, path, extension).df

    # Classe que usa metodos para converter coodenadas para decimal ou dms(gráus, minutos e segundos)
    class convertCoordinates:
        def to_dms():
            print('convertido para dms')
        
        def to_decimal():
            print('convertido para decimal')
            
    
    # Vai receber o objeto/DataFrame criado e formatado, o caminho e o nome do arquivo que será salvo.
    def save(self, filename:str):
        path = 'Data'
        if not os.path.exists(path):
            os.mkdir(path)
        
        self.df.to_excel(f'{path}/{filename}.xlsx', index=False)

    