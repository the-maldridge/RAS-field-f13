import curses
import fullWin
import button
import toggleButton
import textLabel
import timeBox

def buttonExample(): #
    pass

class MainWindow ( fullWin.FullWindow ):
    def __init__ ( self ):
        fullWin.FullWindow.__init__( self )
        self.tLabel = textLabel.TextLabel ( self, 0, 0, "Label" )
        self.tButton = toggleButton.ToggleButton ( self, 0, 10, 3, "Foo", "Bar")
        self.tButton.setPressFunc(buttonExample)

        self.startButton = button.Button ( self, 3, 1, "Start" )
        self.stopButton = button.Button ( self, 3, 10, "Stop" )
        self.resetButton = button.Button ( self, 3, 19, "Reset" )
        self.tBox = timeBox.TimeBox ( self, 8, 1 )

    def parseInput(self, value):
        #if it was a tab, then call self.setFocus(name of thing) -- SAME THING IN RANKWIN
        fullWin.FullWindow.parseInput(self, value)

def main ( screen ):
    m = MainWindow()
    screen.timeout ( 10 )
    screen.hline ( 22, 0, '-', 80 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.KEY_HOME:
            break
        elif myin == ord ( 'j' ):
            m.tButton.toggle()
        else:
            m.update()

if __name__ == "__main__":
    curses.wrapper ( main )
