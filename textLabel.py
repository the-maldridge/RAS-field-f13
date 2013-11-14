import curses

class TextLabel:
    def __init__ ( self, parent, y, x, length, text ):
        self.__dict__['win'] = parent.derwin ( 1, length + 1, y, x )
        self.text = text

        self.draw()
    
    def draw ( self ):
        self.win.addstr ( 0, 0, self.text )
        self.win.refresh()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

def main ( screen ):
    tLabel = TextLabel ( screen, 5, 10, 5, "Label" )
    screen.vline ( 0, 80, '|', 80 )
    while ( True ):
        myin = screen.getch()
        break

if __name__ == "__main__":
    curses.wrapper ( main )
