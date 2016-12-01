# cding: utf-8

import os, time


def inicio():
		print("*" * 20)
		print("{0}{1}".format(format('*', ' <1'), format('*', ' >19')))
		print("{0}{1}{2}".format(format('*', ' <1'), format('SAQUE 24 HORAS',' ^18'), format('*', ' >1')))
		print("{0}{1}".format(format('*', ' <1'), format('*', ' >19')))
		print(("*" * 20))
		print("\n")
		
def saque():
	valor_saque = input("Quanto deseja sacar?: ")
	os.system("clear")
	print("Valor solicitado: R$ {0},00\nAguarde um momento por favor...\n".format(valor_saque))
	time.sleep(3)
	print("Saque autorizado.\nEstamos efetuando a contagem das notas...\n")
	time.sleep(3)
	return int(valor_saque)

def novo_saque():
	print("\n\nDeseja efetuar outro saque?\n")
	print("*" * 16)
	print("{0}{1}".format(format('*', ' <1'), format('*', ' >15')))
	print("{0}{1}{2}".format(format('*', ' <1'), format("1 - SIM", "^14"), format('*', ' >1')))
	print("{0}{1}{2}".format(format('*', ' <1'), format("2 - NÃO", "^14"), format('*', ' >1')))
	print("{0}{1}".format(format('*', ' <1'), format('*', ' >15')))
	print("*" * 16)
	print()