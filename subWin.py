import curses

class SubWindow:
    def __init__ ( self, parent, y, x ):
        self.__dict__['win'] = parent.derwin ( y, x )
        self.parent = parent
        self.focus = self

    def parseInput ( self ):
        pass

    def update ( self ):
        self.win.touchwin()
        self.win.syncup()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )
