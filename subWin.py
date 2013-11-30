import curses

class SubWindow:
    def __init__ ( self, parent, y, x, rows = None, cols = None ):
        if rows is not None:
            self.__dict__['win'] = parent.derwin ( rows, cols, y, x )
        else:
            self.__dict__['win'] = parent.derwin ( y, x )
        self.parent = parent
        self.focus = self
        self.isfocused = False

    def parseInput ( self, value ):
        pass

    def setFocus ( self, focus ):
        if self.focus is not self:
            self.focus.isfocused = False
        self.focus = focus
        self.focus.isfocused = True

    def update ( self ):
        self.win.syncup()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )
