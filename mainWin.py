import curses
import fullWin
import button
import toggleButton
import textLabel
import timeBox

class MainWindow ( fullWin.FullWindow ):
    def __init__ ( self ):
        fullWin.FullWindow.__init__( self )
        self.tLabel = textLabel.TextLabel ( self, 0, 0, "Label" )
        self.tButton = toggleButton.ToggleButton ( self, 0, 10, 3, "Foo", "Bar" )
        self.startButton = button.Button ( self, 3, 1, "Start" )
        self.stopButton = button.Button ( self, 3, 10, "Stop" )
        self.resetButton = button.Button ( self, 3, 19, "Reset" )
        self.tBox = timeBox.TimeBox ( self, 8, 1 )

    def update ( self ):
        self.tLabel.draw()
        self.startButton.draw()
        self.stopButton.draw()
        self.resetButton.draw()
        self.tButton.draw()
        self.tBox.update()

        self.tLabel.refresh()
        self.tButton.refresh()
        self.startButton.refresh()
        self.stopButton.refresh()
        self.resetButton.refresh()
        self.tBox.refresh()

        fullWin.FullWindow.update ( self )

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
