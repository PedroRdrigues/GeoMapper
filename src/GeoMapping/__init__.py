# Encurtador de imports
from .formatSpreadSheet import FormatSpreadSheet

"""
EXEMPLE:
from MapeAR import FormatSpreadSheet as fss

# Coleta do caminho do arquivo de origem .csv, .xlsx ou .xls (por enquanto)
nazare = fss('origin/Nazaré csv.csv')

# Método que faz os tratamentos necessários para a arborização
nazare.afforestation()

# Salva e nomeia o arquivo .xlsx (Terá a opção de transformar em GEOJSON no futuro)
nazare.save('Arborizacao_Nazare') 
"""




try:
    import pandas
except:
    raise ModuleNotFoundError("Necessário a instalação do pandas para a utilização")

try:
    import unidecode
except:
    raise ModuleNotFoundError("Necessário a instalação do unidecode para a utilização")