import curses
import subWin

class FullWindow:
    def __init__ ( self ):
        self.__dict__['win'] = curses.newwin ( 0, 0 )
        self.elements = {}
        self.focus = self
        self.isfocused = False

    def parseInput ( self, value ):
        if self.focus is not self:
            self.focus.parseInput(value)

    def update ( self ):
        for element in self.elements.itervalues():
            element.update()
        self.win.refresh()

    def setFocus ( self, focus ):
        if self.focus is not self:
            self.focus.isfocused = False
        self.focus = focus
        self.focus.isfocused = True

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
