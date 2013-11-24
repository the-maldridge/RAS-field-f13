import curses
import subWin

class TextField ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x, length, text = None ):
        subWin.SubWindow.__init__( self, parent, y, x, 1, length + 1 )
        if ( text is None ):
            self.text = " " * length
        else:
            self.text = text

    def update ( self ):
        self.win.clear()
        self.win.addstr ( 0, 0, self.text, curses.A_UNDERLINE )

        subWin.SubWindow.update ( self )

def main ( screen ):
    tField = TextField ( screen, 5, 10, length = 10 )
    screen.vline ( 0, 78, '|', 80 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            tField.update()
            screen.refresh()
        else:
            break

if __name__ == "__main__":
    curses.wrapper ( main )
