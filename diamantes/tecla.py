# coding:utf-8

import sys, os

import curses
import curses.textpad
import time

stdscr = curses.initscr()

c = stdscr.getch()
#    if c == ord('p'): 
if c == ord('q'): print(c)
#    elif c == curses.KEY_HOME: x = y = 0
else: print('não deu')


curses.endwin()