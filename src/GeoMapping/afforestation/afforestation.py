# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:42:36 2024

@author: PedroRdrigues
"""

from dataclasses import dataclass
from imports import ImportCsv, ImportExcel


extensionListExcel = ['.xlsx', '.xls', '.xlsm', '.xlsb', '.xltx', '.xltm']


@dataclass()
class Afforestation:
    filename: str
    path: str
    extension: str

    def __post_init__(self):
        if self.extension.lower() == '.csv':
            self.import_csv()

        if self.extension.lower() in extensionListExcel:
            self.import_excel()

    def import_csv(self):
        self.df = ImportCsv(
            self.filename, self.path).df

    def import_excel(self):
        self.df = ImportExcel(
            self.filename, self.path, self.extension).df
