from bs4 import BeautifulSoup
import requests


usual_local_strings = ["Sede", "Endereço"]

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

def findCountry(name):
    print("looking for country or place...")
    if " " in name.strip():
        name = name.strip().replace(" ", "+")

        #log in linkedin
    #create a session
    client = requests.Session()

    #create url page variables
    HOMEPAGE_URL = 'https://www.linkedin.com'
    LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
    CONNECTIONS_URL = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'
    ASPIRING_DATA_SCIENTIEST = 'https://www.linkedin.com/search/results/people/?keywords=Aspiring%20Data%20Scientist&origin=GLOBAL_SEARCH_HEADER'

    #get url, soup object and csrf token value
    html = client.get(HOMEPAGE_URL).content
    soup = BeautifulSoup(html, "html.parser")
    csrf = soup.find('input', dict(name='loginCsrfParam'))['value']

    #create login parameters
    login_information = {
        'session_key':'wiliane_souza@hotmail.com',
        'session_password':'batom123',
        'loginCsrfParam': csrf,
    }

    #try and login
    try:
        client.post(LOGIN_URL, data=login_information)
        print("Login Successful")
    except:
        print("Failed to Login")



        #pegando o link do linkedin da empresa
    try:
        response = client.get(f'https://www.linkedin.com/search/results/all/?keywords={name}')
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        print('Erro ao conectar-se com a página')
        return "?"

    #extraindo link da lista
    try:
        linkedin = soup.select_one("a.search-result__result-link.ember-view").get('href')
    except AttributeError:
        print(soup)
        return "?"

    if linkedin == None:
        print("LINKEDIN N ENCONTRADO")
        return "?"
    
    #Conectando a pág do linkedin da empresa
    try:
        html = requests.get(linkedin)
        soup = BeautifulSoup(html.text, 'html.parser')
    except:
        print('Erro ao conectar-se com a página do linkedin')
        return "?"

    #extraindo localidade:
    info_list = soup.select_one(".org-top-card-summary-info-list").select("div")

    if info_list is not None:
        local = info_list[1].select_one("div").text
        if local is not None:
            return local
        else:
            return "?"
    else:
        print("NAO ENCONTRADO")
        return "?"

    