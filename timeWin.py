import time
import curses
import pyfiglet

class TimeWin:
    def __init__ ( self, parent, y, x ):
        self.__dict__['win'] = parent.derwin ( 10, 78, y, x )
        self.update()

    def update ( self ):
        self.win.clear()
        self.win.box()
        t = time.time()
        t_string = pyfiglet.figlet_format ( str ( t ), font = "big" )
        for i, line in enumerate ( t_string.rstrip().split('\n') ):
            self.win.addstr ( 1 + i, 2, line )

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

def main ( screen ):
    tWin = TimeWin ( screen, 0, 0 )
    screen.vline ( 0, 80, '|', 80 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            tWin.update()
            tWin.refresh()
        else:
            break

curses.wrapper ( main )
