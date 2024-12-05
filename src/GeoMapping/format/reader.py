# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:42:36 2024

@author: PedroRdrigues
"""

from dataclasses import dataclass
from .readers import ReadExcel, ReadCsv


extensionListExcel = ['.xlsx', '.xls', '.xlsm', '.xlsb', '.xltx', '.xltm']


@dataclass()
class Reader:
    filename: str
    path: str
    extension: str

    def __post_init__(self):
        if self.extension.lower() == '.csv':
            self.csv()

        if self.extension.lower() in extensionListExcel:
            self.excel()

    def csv(self):
        self.df = ReadCsv(
            self.filename, self.path).df

    def excel(self):
        self.df = ReadExcel(
            self.filename, self.path, self.extension).df
