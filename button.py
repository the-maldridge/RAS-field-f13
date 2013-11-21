import curses
class Button:
    def __init__ ( self, parent, y, x, text = "" ):
        self.__dict__['win'] = parent.derwin ( 3, len ( text ) + 2, y, x )
        self.text = text
        self.draw()

    def draw ( self ):
        self.win.box()
        self.win.addstr ( 1, 1, self.text )

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

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

if __name__ == "__main__":
    curses.wrapper ( main )

