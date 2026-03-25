"""
Programa soma
Descrição: Este programa lê dois números do teclado, calcula a soma e coloca o resultado na tela.
Autor: Filipe
Data: 24/03/2026
Versão: 0.0.3
"""

#alocação de memória
num1 = 0
num2 = 0
r = 0
i = 0

#Entrada de dados

while i < 2:
  num = (int(input(f"Digite o {i + 1}º número: ")))
  r = r + num
  i += 1

print(f"O resultado da soma é {r}")

input("Pressione enter para sair ...")
