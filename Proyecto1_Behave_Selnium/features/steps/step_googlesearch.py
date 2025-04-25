from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import *
import time

# Given el usuario abre el navegador Chrome
driver = webdriver.Chrome()

try:
    # When el usuario navega a Google
    driver.get("https://www.google.com")
    time.sleep(2)

    # Aceptar cookies si aparece el botón (solo en la primera vez o dependiendo del país)
    try:
        aceptar_btn = driver.find_element(By.XPATH, '//button[contains(text(),"Aceptar")]')
        aceptar_btn.click()
        time.sleep(1)
    except:
        pass  # No apareció el botón, seguimos

    # And el usuario busca "Trivago”
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Trivago")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Esperar a que se carguen los resultados

    # Then el título de la página contiene "trivago"
    assert "trivago" in driver.title.lower()
    print("✅ Test PASÓ: El título contiene 'trivago'")
except AssertionError:
    print("❌ Test FALLÓ: El título no contiene 'trivago'")
finally:
    driver.quit()
