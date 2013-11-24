import curses

class FullWindow:
    def __init__ ( self ):
        self.__dict__['win'] = curses.newwin ( 0, 0 )
        self.focus = self

    def getInput ( self ):
        inputKey = self.win.getkey()
        self.focus.parseInput ( inputKey )

    def parseInput ( self ):
        pass

    def update ( self ):
        self.win.refresh()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )
