"""
Criar um programa com selenium que:
    - Jogue o joguinho;
    - quando você ganhar, o script deve parar  de ser execultado.

url: https://curso-python-selenium.netlify.app/exercicio_02.html
"""
# Importando o do selenium o webdriver do firefox
from selenium.webdriver import Firefox
from time import sleep

# Definindo a url a ser acessada
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

# Define o webdriver à variável navegador e abre o navegador
navegador = Firefox()

# Acessa a url
navegador.get(url)
sleep(1)

# Busca o elemento pelo id 'ancora' e armazena na variável a
a = navegador.find_element_by_id('ancora')

# Define uma variável victory como False
victory = False

while victory==False:
    # Clica no a enquanto o loop é execultado
    a.click()
    # Armazena na variável ps todos os elementos com a tag <p>
    ps = navegador.find_elements_by_tag_name('p')

    # Verifica se no último elemento <p> contém a string 'Você ganhou'
    if 'Você ganhou' in ps[-1].text:
        # Caso a condição seja verdadeira, faz um print e altera a variável victory para True, assim finalizando o loop
        print('Parabéns! Você ganhou')
        victory = True

# Fecha o navegador
navegador.quit()
