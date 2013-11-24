import curses
import subWin

class TextArea ( subWin.SubWindow ):
    def __init__ ( self, parent, y, x, height = None, width = None, text = "" ):
        if ( height is not None and width is not None ):
            subWin.SubWindow.__init__( self, parent, y, x, height, width )
        else:
            subWin.SubWindow.__init__( self, parent, y, x )
        self.text = text
        self.curline = 0

    def update ( self ):
        height, width = self.win.getmaxyx()

        self.win.clear()

        self.win.box()
        for i, line in enumerate ( self.text.splitlines()[ self.curline:self.curline + height - 2 ] ):
            self.win.addstr ( i + 1, 1, line )

        subWin.SubWindow.update ( self )
    
    def scroll ( self, dist ):
        if ( dist > 0 and self.curline + dist < len ( self.text.splitlines() ) ):
            self.curline = self.curline + dist
        elif ( dist < 0 and self.curline + dist >= 0 ):
            self.curline = self.curline + dist

def main ( screen ):
    tArea = TextArea ( screen, 1, 1, 24, 80, 
      "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz" )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == ord ( 'j' ):
            tArea.scroll ( 1 )
        elif myin == ord ( 'k' ):
            tArea.scroll ( -1 )
        elif myin == curses.KEY_HOME:
            break
        tArea.update()
        screen.refresh()

if __name__ == "__main__":
    curses.wrapper ( main )
