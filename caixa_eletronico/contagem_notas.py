import os


def contas(valor, cedula):
	if min(valor, cedula) == cedula:
		notas = valor // cedula
		resto = valor % cedula
	else:
		notas = 0
		resto = valor
	return notas, resto

def cont_notas(valor):
	notas_100, resto = contas(valor, 100)
	notas_50, resto = contas(resto, 50)
	notas_20, resto = contas(resto, 20)
	notas_10, resto = contas(resto, 10)

	os.system("clear")
	print("Retire seu dinheiro.\nVocê está recebendo:\n")
	if notas_100 != 0:
		print("Notas de 100: ", notas_100)
	if notas_50 != 0:
		print("Notas de  50: ", notas_50)
	if notas_20 != 0:
		print("Notas de  20: ", notas_20)
	if notas_10 != 0:
		print("Notas de  10: ", notas_10)
