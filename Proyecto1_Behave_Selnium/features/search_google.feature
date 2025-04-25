Feature: Buscar en Google 
Scenario: El usuario busca "Trivago" 
Given el usuario abre el navegador Chrome 
When el usuario navega a Google 
And el usuario busca "Trivago” Then el titulo de la pagina contiene "trivago"