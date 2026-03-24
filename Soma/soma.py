"""
Programa soma
Descrição: Este programa lê dois números do teclado, calcula a soma e coloca o resultado na tela.
Autor: Filipe
Data: 24/03/2026
Versão: 0.0.1
"""

#alocação de memória
num1 = 0
num2 = 0
r = 0

#Entrada de dados

num1 = float(input("Digite o primeiro número da soma: "))

num2 = float(input("Digite o segundo número da soma: "))

#Processamento de dados

r = num1 + num2

#Saida de dados

print(f"O resultado da soma entre {num1} e {num2} é {r}")

input("Pressione enter para sair ...")