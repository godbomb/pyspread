#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2008 Martin Manns
# Distributed under the terms of the GNU General Public License
# generated by wxGlade 0.6 on Mon Mar 17 23:22:49 2008

# --------------------------------------------------------------------
# pyspread is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyspread is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyspread.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
_main_window
============

Provides:
---------
  1) MainWindow: Main window of the application pyspread

"""

import wx
import wx.aui

from config import MAIN_WINDOW_ICON, displaysize

from _menubars import MainMenu
from _toolbars import MainToolbar, FindToolbar, AttributesToolbar
from _widgets import EntryLine, StatusBar, TableChoiceIntCtrl
from _grid import Grid
from _events import *


class MainWindow(wx.Frame):
    """Main window of pyspread"""
    
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)
        
        self._mgr = wx.aui.AuiManager(self)
    
        self.parent = parent
        
        self.handlers = MainWindowEventHandlers(self)
        
        # Menu Bar
        menubar = wx.MenuBar()
        self.main_menu = MainMenu(parent=self, menubar=menubar)
        self.SetMenuBar(menubar)
        
        # Disable menu item for leaving save mode
        self.main_menu.enable_file_approve(False)
        
        # Status bar
        statusbar = StatusBar(self)
        self.SetStatusBar(statusbar)
        
        welcome_text = "Welcome to pyspread."
        post_command_event(self, StatusBarMsg, text=welcome_text)
        
        # Tool bars
        self.main_toolbar = MainToolbar(self, -1)
        self.find_toolbar = FindToolbar(self, -1)
        self.attributes_toolbar = AttributesToolbar(self, -1)
        
        # Entry line
        self.entry_line = EntryLine(self)
        
        # IntCtrl for table choice
        self.table_choice = TableChoiceIntCtrl(self, 1) ## Link to grid dim here!
        
        # Main grid
        
        self._grid = Grid(self, -1)
        
        self._set_properties()
        self._do_layout()
        self._bind()
    
    def _set_properties(self):
        """Setup title, icon, size, scale, statusbar, main grid"""
        
        self.set_icon(MAIN_WINDOW_ICON)
        
        self.SetInitialSize((int(displaysize[0] * 0.9), 
                             int(displaysize[1] * 0.9)))

    def _do_layout(self):
        """Adds widgets to the wx.aui manager and controls the layout"""
        
        # Add the toolbars to the manager
        self._mgr.AddPane(self.main_toolbar, wx.aui.AuiPaneInfo().
                          Name("main_window_toolbar").Caption("Main Toolbar").
                          ToolbarPane().Top().Row(0).CloseButton(False).
                          LeftDockable(False).RightDockable(False))
                                  
        self._mgr.AddPane(self.find_toolbar, wx.aui.AuiPaneInfo().
                          Name("find_toolbar").Caption("Find").
                          ToolbarPane().Top().Row(1).MaximizeButton(False).
                          LeftDockable(False).RightDockable(False))
        
        self._mgr.AddPane(self.attributes_toolbar, wx.aui.AuiPaneInfo().
                          Name("attributes_toolbar").Caption("Cell Attributes").
                          ToolbarPane().Top().Row(1).MaximizeButton(False).
                          LeftDockable(False).RightDockable(False))
                          
                          
        self._mgr.AddPane(self.table_choice, wx.aui.AuiPaneInfo().
                          Name("table_choice").Caption("Table choice").
                          ToolbarPane().MaxSize((50, 50)).Row(2).
                          Top().CloseButton(False).MaximizeButton(False).
                          LeftDockable(True).RightDockable(True))
        
        self._mgr.AddPane(self.entry_line, wx.aui.AuiPaneInfo().
                          Name("entry_line").Caption("Entry line").
                          ToolbarPane().MinSize((10, 10)).Row(2).
                          Top().CloseButton(False).MaximizeButton(False).
                          LeftDockable(True).RightDockable(True))
        
        # Add the main grid
        self._mgr.AddPane(self._grid, wx.CENTER)
        
        # Tell the manager to 'commit' all the changes just made
        self._mgr.Update()
    
    def _bind(self):
        """Bind events to handlers"""
        
        self.Bind(wx.EVT_CLOSE, self.handlers.OnClose)
        self.Bind(EVT_COMMAND_CLOSE, self.handlers.OnClose)
        
        self.Bind(EVT_COMMAND_MANUAL, self.handlers.OnManual)
        self.Bind(EVT_COMMAND_TUTORIAL, self.handlers.OnTutorial)
        self.Bind(EVT_COMMAND_FAQ, self.handlers.OnFaq)
        self.Bind(EVT_COMMAND_ABOUT, self.handlers.OnAbout)
        
        self.Bind(EVT_COMMAND_MACROLIST, self.handlers.OnMacroList)
        self.Bind(EVT_COMMAND_MACROLOAD, self.handlers.OnMacroListLoad)
        self.Bind(EVT_COMMAND_MACROSAVE, self.handlers.OnMacroListSave)
    
    def set_icon(self, bmp):
        """Sets main window icon to given wx.Bitmap"""
        
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(bmp)
        self.SetIcon(_icon)

# End of class MainWindow

class MainWindowEventHandlers(object):
    """Contains main window event handlers"""
    
    def __init__(self, parent):
        self.main_window = parent
    
    # Main window events
    
    def OnTitle(self, event):
        """Title change event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnClose(self, event):
        """Program exit event handler"""
        
        self.main_window._mgr.UnInit()
        
        # Delete the frame
        self.main_window.Destroy()
    
    # Help events
    
    def OnManual(self, event):
        """Manual launch event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnTutorial(self, event):
        """Tutorial launch event handler"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnFaq(self, event):
        """FAQ launch event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnAbout(self, event):
        """About dialog event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    # Macro events
    
    def OnMacroList(self, event):
        """Macro list dialog event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnMacroListLoad(self, event): 
        """Macro list load event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnMacroListSave(self, event):
        """Macro list save event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
# End of class MainWindowEventHandlerMixin
