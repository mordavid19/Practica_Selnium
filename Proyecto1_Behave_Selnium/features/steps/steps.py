from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import *


@given('el usuario abre el navegador Chrome')
def step_impl(context):
    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

@when('el usuario navega a una página de chistes')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get('https://rieconmigo.com/chistes-de-profesor-de-ciencias/#chistes_cortos')
    context.driver.implicitly_wait(10)  # Espera implícita de 10 segundos

@then('el título de la página contiene "{titulo}"')
def step_impl(context, titulo):
    assert titulo in context.driver.title
