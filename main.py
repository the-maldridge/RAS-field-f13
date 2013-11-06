#!/usr/bin/env python

import logging
import timing
import matchdb
import GUI
import wx

class MainWindow(GUI.MainWindow):
    def matchAssignPenalty(self,e):
        print "made it this far"

class GUIMain(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrame = MainWindow(None, -1, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        self.mainFrame = mainFrame
        return 1

class RASScoreboard(GUIMain):
    pass

if __name__ == "__main__":
    theapp = RASScoreboard()
    theapp.MainLoop()
