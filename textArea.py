import curses

class TextArea:
    def __init__ ( self, parent, y, x, height = None, width = None, text = "" ):
        if ( height is not None and width is not None ):
            self.__dict__['win'] = parent.derwin ( height, width, y, x )
        else:
            self.__dict__['win'] = parent.derwin ( y, x )
        self.text = text
        self.curline = 0
        self.update()

    def update ( self ):
        height, width = self.win.getmaxyx()

        self.win.clear()

        for i, line in enumerate ( self.text.splitlines()[ self.curline:self.curline + height - 1 ] ):
            self.win.addstr ( i, 0, line )
        self.win.addstr ( 5, 5, str ( self.curline ) )
        self.win.addstr ( 6, 5, str ( len ( self.text.splitlines() ) ) )
        self.win.refresh()
    
    def scroll ( self, dist ):
        if ( dist > 0 and self.curline + dist < len ( self.text.splitlines() ) ):
            self.curline = self.curline + dist
        elif ( dist < 0 and self.curline + dist >= 0 ):
            self.curline = self.curline + dist
        self.update()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

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

if __name__ == "__main__":
    curses.wrapper ( main )
