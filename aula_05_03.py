from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_c.html')

def melhor_filme(browser, filme, email, telefone):
    """
    Preenche o formulário do melhor filme de 2020a
    """
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

melhor_filme(
    firefox, 
    'Parasita', 
    'matheus@mail.com', 
    '(081)985451247'
    )