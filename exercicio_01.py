"""
Criar um programa com selenium que:
    - Gere um dicionário onde a chave é a tag h1
        - O valor deve ser um novo dicionário;
        - cada chave do valor deverá ser o valor de 'atributo';
        - cada valor deve ser o texto contido no elemento

url: https://curso-python-selenium.netlify.app/exercicio_01.html
"""
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador = Firefox()

navegador.get(url)
sleep(1)

h1 = navegador.find_element_by_tag_name('h1')

dicio = {h1.text: {}}

ps = navegador.find_elements_by_tag_name('p')
for p in ps:
    atributo_p = p.get_attribute('atributo')
    txt_p = p.text
    dicio[h1.text][atributo_p] = txt_p

# print(f'p: {p}\natributo: {atributo_p}\ntexto: {txt_p}')
print(dicio)

navegador.quit()
