from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

firefox = Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05.html')

# nome, email, senha, telefone, btn

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

sleep(2)

estrutura = {
    'nome': 'Matheus', 
    'email': 'matheus@email.com', 
    'senha': '123456', 
    'telefone': '81985451247'
}

preenche_form(firefox, **estrutura)

url_parseada = urlparse(firefox.current_url)

sleep(2)

texto_resultado = firefox.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dict_result = loads(resultado_arrumado)

assert dict_result == estrutura