import curses
import types
import subWin

class ToggleButton ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x, length, text1, text2 ):
        self.__dict__['win'] = parent.derwin ( 3, length + 2, y, x )
        subWin.SubWindow.__init__( self, parent, y, x, 3, length + 2 )
        self.text1 = text1
        self.text2 = text2

        self.state = False

    def update ( self ):
        self.win.standend()
        self.win.box()
        if self.state:
            self.win.standout()
            self.win.addstr ( 1, 1, self.text2 )
        else:
            self.win.addstr ( 1, 1, self.text1 )

        subWin.SubWindow.update ( self )

    def toggle ( self ):
        if self.state:
            self.state = False
        else:
            self.state = True
        self.press()

    def press ( self ):
        pass

    def setPressFunc ( self, f ):
        self.press = types.MethodType ( f, self )

def main ( screen ):
    tButton = ToggleButton ( screen, 5, 10, 3, "Foo", "Bar" )
    screen.vline ( 0, 80, '|', 80 )
    while ( True ):
        tButton.update()
        screen.refresh()
        myin = screen.getch()
        if myin != curses.KEY_HOME:
            tButton.toggle()
        else:
            break

if __name__ == "__main__":
    curses.wrapper ( main )
