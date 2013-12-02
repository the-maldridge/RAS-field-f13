import curses
import button
import subWin

class PenaltyWindow ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x, height = None, width = None ):
        if ( height is not None and width is not None ):
            if height + y > 24 or width + x > 80:
                raise curses.error
            if height < 9 or width < 42:
                raise curses.error
            subWin.SubWindow.__init__( self, parent, y, x, height, width )
        else:
            subWin.SubWindow.__init__( self, parent, y, x )

        self.button1 = button.Button ( self, 2, 2, "Button1" )
        self.button2 = button.Button ( self, 6, 2, "Button2" )
        self.button3 = button.Button ( self, 1, 20, "Button3" )
        self.button4 = button.Button ( self, 2, 38, "Button4" )
        self.button5 = button.Button ( self, 6, 38, "Button5" )

    def update ( self ):
        self.win.box()
        self.button1.update()
        self.button2.update()
        self.button3.update()
        self.button4.update()
        self.button5.update()

        subWin.SubWindow.update ( self )

def main ( screen ):
    pWin = PenaltyWindow ( screen, 2, 2, 10, 48 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            pass
        else:
            break
        pWin.update()
        screen.refresh()

if __name__ == "__main__":
    curses.wrapper ( main )
