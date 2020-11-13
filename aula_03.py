# Importando o do selenium o webdriver do firefox
from selenium.webdriver import Firefox
from time import sleep

# Definindo a url a ser acessada
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

# Define o webdriver à variável navegador e abre o navegador
navegador = Firefox()

# Acessa a url
navegador.get(url)

# Espera 1 segundo (para carregar a página)
sleep(1)

# Busca o elemento pela tag <a> e armazena na variável a
a = navegador.find_element_by_tag_name('a')

# Inicia um loop a ser executado 10 vezes
for click in range(10):
    # Encontra todos os elementos com a tag <p>
    ps = navegador.find_elements_by_tag_name('p')
    # Clica no elemento da tag <a>
    a.click()
    
    print(f'Valor ultimo p: {ps[-1].text} valor do click: {click}')
    print(f'Os valores são iguais {int(ps[-1].text) == click}')

# Fecha o navegador
navegador.quit()
