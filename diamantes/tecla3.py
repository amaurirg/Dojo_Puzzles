# import time
import curses

stdscr = curses.initscr()
# curses.halfdelay(10) # 10/10 = 1[s] inteval

try:
    while True:
        c = stdscr.getch()
        if c != -1:
        	stdscr.addstr(" -> A tecla %s foi pressionada e seu código é %s\n" % (chr(c), str(c)))
        # stdscr.addstr("time() == %s\n" % time.time())
finally:
    curses.endwin()