import curses
import subWin

class FullWindow:
    def __init__ ( self ):
        self.__dict__['win'] = curses.newwin ( 0, 0 )
        self.focus = self
        self.elements = {}

    def parseInput ( self ):
        pass

    def update ( self ):
        for element in self.elements.itervalues():
            element.update()
        self.win.refresh()

    def __setattr__ ( self, attr, value ):
        if attr in self.__dict__.keys():
            self.__dict__[ attr ] = value
            return value
        elif isinstance ( value, subWin.SubWindow ):
            self.elements[ attr ] = value
            self.__dict__[ attr ] = value
            return value
        else:
            self.__dict__[ attr ] = value
            return value

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )
