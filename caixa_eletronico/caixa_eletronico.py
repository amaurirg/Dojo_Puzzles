# coding: utf-8
"""
Caixa Eletrônico

Este problema foi utilizado em 588 Dojo(s).

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. 
Os requisitos básicos são os seguintes:
Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:
Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
"""

import os
import info_user, contagem_notas

resp = 1

while resp != '2':
	os.system("clear")
	info_user.inicio()
	valor_solicitado = info_user.saque()
	contagem_notas.cont_notas(valor_solicitado)
	info_user.novo_saque()
	resp = input()

os.system("clear")
print("Obrigado por utilizar o Caixa 24 Horas.\n\nTenha um ótimo dia!\n")
