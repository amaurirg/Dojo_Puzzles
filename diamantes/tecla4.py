import curses


stdscr = curses.initscr()

while True:
    key = stdscr.getch()
    if key == 27:
    	break

curses.endwin()