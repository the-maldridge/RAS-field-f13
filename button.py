import curses
import types
import subWin

class Button ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x, text = "" ):
        subWin.SubWindow.__init__( self, parent, y, x, 3, len ( text ) + 2 )
        self.text = text

    def update ( self ):
        self.win.box()
        self.win.addstr ( 1, 1, self.text )

        subWin.SubWindow.update ( self )

    def press ( self ):
        pass

    def setPressFunc ( self, f ):
        self.press = types.MethodType ( f, self )

def main ( screen ):
    tButton = Button ( screen, 0, 0, "Button" )
    screen.vline ( 0, 78, '|', 80 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            pass
        else:
            break
        tButton.update()

if __name__ == "__main__":
    curses.wrapper ( main )

