import requests
from bs4 import BeautifulSoup
import json

# URL do site que você quer fazer scraping
url = 'https://www.basketball-reference.com/leagues/NBA_2025_per_game.html#per_game_stats'

# Enviar uma requisição HTTP para o site
response = requests.get(url)

# Criar um objeto BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extrair todos os títulos de artigos
tabelas = soup.find_all('table')
for tabela in tabelas:
    print(tabela)

linhas = tabela.find_all('tr')

dados= [ ]
for linha in linhas:
    celulas = linha.find_all('td')
    dados_linha = [celula.get_text(strip=True) for celula in celulas]
    dados.append(dados_linha)

# Exibir os dados extraídos
for linha in dados:
    print(linha)


dados_json = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o JSON
print(dados_json)



with open('dados_tabela.json', 'w', encoding='utf-8') as f:
    f.write(dados_json)

print("Os dados foram salvos no arquivo 'dados_tabela.json'.")