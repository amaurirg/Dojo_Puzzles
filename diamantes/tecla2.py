import curses
from curses import ascii

letra = int(input("LETRA: "))
print(curses.ascii.unctrl(letra))