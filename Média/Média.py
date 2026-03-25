"""
Programa média
Descrição Este programa lê a quantidade definida pelo usuário de números do teclado, calcula a média e coloca o resultado na tela.
Autor Filipe
Data 24/03/2026
Versão 0.0.1
"""

#alocação de memória
j = 0
i = 1
num = 0
soma = 0

#Entrada de dados
j = int(input("Digite a quantidade de números que quer fazer a média: "))

while i <= j:
	num = int(input(f"Digite o {i}º número: "))
	soma = soma + num
	i += 1
	

#Saida
print(f"O resultado da média é {soma/j}")

input("Pressione enter para sair ...")