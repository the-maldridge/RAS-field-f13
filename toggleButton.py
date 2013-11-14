import curses

class ToggleButton:
    def __init__ ( self, parent, y, x, length, text1, text2 ):
        self.__dict__['win'] = parent.derwin ( 1, length + 1, y, x )
        self.text1 = text1
        self.text2 = text2

        self.text = text1

        self.win.standout()

        self.draw()
    
    def toggle ( self ):
        if self.text == self.text1:
            self.text = self.text2
        else:
            self.text = self.text1
        self.draw()

    def draw ( self ):
        self.win.addstr ( 0, 0, self.text )
        self.win.refresh()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

def main ( screen ):
    tButton = ToggleButton ( screen, 5, 10, 4, "Foo", "Bar" )
    screen.vline ( 0, 80, '|', 80 )
    while ( True ):
        myin = screen.getch()
        if myin != curses.KEY_HOME:
            tButton.toggle()
        else:
            break

if __name__ == "__main__":
    curses.wrapper ( main )
