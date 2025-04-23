Feature: Mostrar página web
  Scenario: El usuario abre una página de chistes
    Given el usuario abre el navegador Chrome
    When el usuario navega a una página de chistes
    Then el título de la página contiene "chistes"
