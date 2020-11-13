"""
Criar um programa com selenium que:
    - Gere um dicionário onde a chave é a tag h1
        - O valor deve ser um novo dicionário;
        - cada chave do valor deverá ser o valor de 'atributo';
        - cada valor deve ser o texto contido no elemento

url: https://curso-python-selenium.netlify.app/exercicio_01.html
"""
# Importando o do selenium o webdriver do firefox
from selenium.webdriver import Firefox
from time import sleep

# Definindo a url a ser acessada
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

# Define o webdriver à variável navegador e abre o navegador
navegador = Firefox()

# Acessa a url
navegador.get(url)
sleep(1)

# Busca o elemento pela tag <h1> e armazena na variável h1
h1 = navegador.find_element_by_tag_name('h1')

# Cria um dicionário que tem como chave o texto contido na tag h1 e como valor outro dicionário
dicio = {h1.text: {}}

# Encontra todos os elementos com a tag <p>
ps = navegador.find_elements_by_tag_name('p')
for p in ps:
    # Encontra o atributo 'atributo' dentro da tag p e armazena na variável
    atributo_p = p.get_attribute('atributo')
    # Encontra o texto contido na tag <p> e armazena na variável
    txt_p = p.text
    # Armazena no dicionário(valor da chave 'h1.text' dentro do dicionário dicio)
    # o atributo como chave e seu conteúdo como valor
    dicio[h1.text][atributo_p] = txt_p

# Printa o dicionário
print(dicio)

# Fecha o navegador
navegador.quit()
