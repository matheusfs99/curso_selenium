"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04.html')

def get_links(browser, elemento):  # dicionário
    '''
    pega todos os links dentro de um elemento

    - browser = a instancia do navegador
    - elemento = webelement [aside, main, body, ul, ol]
    '''
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')
    return resultado

"""
Parte 1
"""
sleep(2)

aulas = get_links(browser, 'aside')

pprint(aulas)

"""
browser.get(resultado_1['Aula 3'])
browser.get(resultado_1['Aula 4'])
"""


"""
Parte 2
"""
exercicios = get_links(browser, 'main')

pprint(exercicios)

browser.get(exercicios['Exercício 3'])