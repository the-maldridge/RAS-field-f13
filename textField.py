import curses

class TextField:
    def __init__ ( self, parent, y, x, length, text = None ):
        self.__dict__['win'] = parent.derwin ( 1, length + 1, y, x )
        if ( text is None ):
            self.text = " " * length
        else:
            self.text = text
        self.update()

    def update ( self ):
        self.win.clear()
        self.win.addstr ( 0, 0, self.text, curses.A_UNDERLINE )

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

def main ( screen ):
    tField = TextField ( screen, 5, 10, length = 10 )
    screen.vline ( 0, 78, '|', 80 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            tField.update()
            tField.refresh()
        else:
            break

if __name__ == "__main__":
    curses.wrapper ( main )
