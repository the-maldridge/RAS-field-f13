import curses
class Button:
    def __init__ ( self, parent, y, x, text = "" ):
        self.__dict__['win'] = parent.derwin ( 3, len ( text ) + 2, y, x )
        self.win.box()
        self.win.addstr ( 1, 1, text )

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )
