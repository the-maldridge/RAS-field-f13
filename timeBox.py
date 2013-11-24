import time
import curses
import subWin
import pyfiglet

class TimeBox ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x ):
        self.__dict__['win'] = parent.derwin ( 10, 78, y, x )
        subWin.SubWindow.__init__( self, parent, y, x, 10, 78 )

    def update ( self ):
        self.win.clear()
        self.win.box()
        t = time.time()
        t_string = pyfiglet.figlet_format ( str ( t ), font = "big" )
        for i, line in enumerate ( t_string.rstrip().split('\n') ):
            self.win.addstr ( 1 + i, 2, line )

        subWin.SubWindow.update ( self )

def main ( screen ):
    tBox = TimeBox ( screen, 0, 0 )
    screen.vline ( 0, 78, '|', 80 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            tBox.update()
            screen.refresh()
        else:
            break

if __name__ == "__main__":
    curses.wrapper ( main )
