# coding: utf-8

"""
Este problema foi utilizado em 156 Dojo(s).
Funcionários de empresas comerciais que trabalham como caixa tem uma grande responsabilidade em suas mãos. A maior parte do tempo de seu expediente de trabalho é gasto recebendo valores de clientes e, em alguns casos, fornecendo troco.
Seu desafio é fazer um programa que leia o valor total a ser pago e o valor efetivamente pago, informando o menor número de cédulas e moedas que devem ser fornecidas como troco.
Deve-se considerar que há:
cédulas de R$100,00, R$50,00, R$10,00, R$5,00 e R$1,00;
moedas de R$0,50, R$0,10, R$0,05 e R$0,01.
"""

# valor = int(input("Digite o valor da compra: "))
# dinheiro = int(input("Quanto foi recebido: "))
# troco = dinheiro - valor
# print("O troco é: R$ {0},00".format(troco))


def calculo(dinheiro, valor):
	return int(dinheiro) - int(valor)

assert calculo('100', '40') == 60
