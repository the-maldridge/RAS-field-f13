import curses

class SubWindow:
    def __init__ ( self, parent, y, x, rows = None, cols = None ):
        if rows is not None:
            self.__dict__['win'] = parent.derwin ( rows, cols, y, x )
        else:
            self.__dict__['win'] = parent.derwin ( y, x )
        self.parent = parent
        self.focus = self

    def parseInput ( self, value ):
        pass

    def update ( self ):
        self.win.syncup()

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )
