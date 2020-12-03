from bs4 import BeautifulSoup
import requests
import pandas as pd

#  ---- Minhas funções e classes
from Export import export_df
from CountryScraper import findCountry

data = { # -> diciionário para data frame 
    'Company': [],
    'WFH': [],
    'Travel': [],
    'Visitors': [],
    'Events': [],
    'Last Update': [],
    'Company Country': [],
}

def stayingHomeScraper():
    html = requests.get('https://stayinghome.club/companies.html')
    soup = BeautifulSoup(html.text, 'html.parser')

    #Numero de empresas
    num_comp = 20

    #Tabela com os dados:
    table_lines = soup.find("tbody").select("tr")

                    #Análise da tabela

    for line in table_lines:
        line_columns = line.select("td")
       
        #retirando marcadores do nome da empresa
        name_company = line_columns[0].text.strip()
        for i in range(1, 10):
            if f"[{i}]" in name_company:
                name_company = name_company.replace(f"[{i}]", "").strip()
            else:
                break

        #Inserindo dados no data frame
        data['Company'].append(name_company)
        data['WFH'].append(line_columns[1].text.strip())
        data['Travel'].append(line_columns[2].text.strip())
        data['Visitors'].append(line_columns[3].text.strip())
        data['Events'].append(line_columns[4].text.strip())
        data['Last Update'].append(line_columns[5].text.strip())
        
            #Inserindo localidade usando scraper:
        data['Company Country'].append(findCountry(name_company))

        break
        if len(data['Company']) >= 20:
            break
    
    print(data)


    if len(data['Company']) > 0: #se algum resultado for capturado

        # ---- Salvando resultado
        df = pd.DataFrame(data, columns = ['Company', 'WFH', 'Travel', 'Visitors', 'Events', 'Last Update', 'Company Country']) #-> criando dataframe

        # ---- Exportando para excel (xlsx) e/ou csv
        export_df(df, 'xlsx', 'csv', wb='SH')


stayingHomeScraper()

print('FIM DA EXECUÇÃO')

    