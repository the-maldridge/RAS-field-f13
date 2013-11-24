import curses
import fullWin
import textArea

class rankWindow ( fullWin.FullWindow ):
    def __init__ ( self, text = "" ):
        fullWin.FullWindow.__init__( self )
        self.rankArea = textArea.TextArea ( self, 0, 0, 24, 80, text )

def main ( screen ):
    r = rankWindow( "Team A\n" +
                    "Team B\n" +
                    "Team C\n" +
                    "Team D\n" +
                    "Team E\n" +
                    "Team F\n" +
                    "Team G\n" +
                    "Team H\n" +
                    "Team I\n" +
                    "Team J\n" +
                    "Team K\n" +
                    "Team L\n" +
                    "Team M\n" +
                    "Team N\n" +
                    "Team O\n" +
                    "Team P\n" +
                    "Team Q\n" +
                    "Team R\n" +
                    "Team S\n" +
                    "Team T\n" +
                    "Team U\n" +
                    "Team V\n" +
                    "Team W\n" +
                    "Team X\n" +
                    "Team Y\n" +
                    "Team Z\n")
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.KEY_DOWN or myin == ord ( 'j' ):
            r.rankArea.scroll ( 1 )
        elif myin == curses.KEY_UP or myin == ord ( 'k' ):
            r.rankArea.scroll ( -1 )
        elif myin == curses.KEY_HOME:
            break
        r.update()

if __name__ == "__main__":
    curses.wrapper ( main )
