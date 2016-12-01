"""
Este problema foi utilizado em 94 Dojo(s).
Dado uma letra ('A' a 'Z'), exiba um diamante iniciando em 'A' e tendo a letra fornecida com o ponto mais distante.
Por exemplo, dado a letra 'E' temos:
    A   
   B B
  C   C
 D     D
E       E 
 D     D 
  C   C
   B B
    A
 
Dado a letra 'C' temos:
  A
 B B
C   C
 B B
  A

# print(len(alfabeto)) = 26  
"""

import string
import curses


alfabeto = list(string.ascii_uppercase)

def diamante(letra):
	indice = alfabeto.index(letra)
	lista = [item for item in alfabeto[:indice+1]]
	lista += lista[indice-1::-1]
	for item in lista:
		if item == 'A':
			print(' '*(lista.index(letra)-lista.index(item))+item)
		else:	
			print(' '*(lista.index(letra)-lista.index(item))+item+(' '*((lista.index(item)*2)-1))+item)

running = True

while running:
	letra_escolhida = input("\nEscolha uma letra do alfabeto: ")
	if letra_escolhida.isalpha():
		diamante(letra_escolhida.upper())
	else:
		print("Você não digitou uma letra correspondente ao alfabeto!\nTente novamente.\n")
	# continuar = input("Digite uma letra para continuar ou ESC para sair")
	print("Digite uma letra para continuar ou ESC para sair: ")
	stdscr = curses.initscr()
	stdscr.getch()
	key = stdscr.getch()
	# key = continuar
	if key == 27:
		running = False
		curses.endwin()
		break
	else:
		curses.endwin()
		continue

