from bs4 import BeautifulSoup
import requests


usual_local_strings = ["Sede", "Endereço"]

# ---- Work in progress 
#* Google -> not working so far (?)
#* Linkedin -> fail -> does not allow scraping | ip may be blocked | needs to be logged

#
""" print("looking for country or place...")
    if " " in name.strip():
        name = name.strip().replace(" ", "+")
    
        #Primeira tentativa
    try:
        html = requests.get(f'http://www.google.com/search?q={name}+company')
        soup = BeautifulSoup(html.text, 'html.parser')
    except:
        print('Erro ao conectar-se com a página')
        return -1

    for local_str in usual_local_strings:
        tag = soup.select_one('td:contains("{local_str}")')
        print(tag)
        if tag != None:
            print(f"1 - {local_str}")
            return tag.findNext('span').text

    
        #Segunda tentativa
    try:
        html = requests.get(f'http://www.google.com/search?q={name}')
        soup = BeautifulSoup(html.text, 'html.parser')
    except:
        print('Erro ao conectar-se com a página')
        return -1

    for local_str in usual_local_strings:
        tag = soup.select_one('td:contains("{local_str}")')
        print(tag)
        if tag != None:
            print(f"2 - {local_str}")
            return tag.findNext('span').text

    print("NAO ENCONTRADO")
    return "?"
"""