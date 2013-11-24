import curses
import subWin

class TextLabel ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x, text ):
        subWin.SubWindow.__init__ ( self, parent, y, x, 1, len ( text ) + 1 )
        self.text = text
    
    def update ( self ):
        self.win.addstr ( 0, 0, self.text )
        
        subWin.SubWindow.update ( self )

def main ( screen ):
    tLabel = TextLabel ( screen, 5, 10, "Label" )
    screen.vline ( 0, 78, '|', 80 )
    tLabel.update()
    screen.refresh()
    while ( True ):
        myin = screen.getch()
        break

if __name__ == "__main__":
    curses.wrapper ( main )
