import os
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from libs import initWin
from assets.styles import general as general_style
import actions.main as main_action
from controllers.session import *

def vp_start_gui():
    global root
    root = tk.Tk()
    top = main (root)
    initWin.init(root, top)
    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.mainloop()
    

class main:
    
    def __init__(self, top=None):
        self.top = top
        self.init()

    def makeMenu(self):
        self.menubar = tk.Menu(
            self.top,
            font = general_style.f10,
            bg = general_style.bgcolor,
            fg = general_style.fgcolor
        )
        self.top.configure(menu = self.menubar)

        self.menubar.add_command(
            background=general_style.bgcolor,
            command= main_action.mnu_tablero,
            font=general_style.f10,
            label="Tablero",
            state="disabled"
        )
        self.menubar.add_command(
            background=general_style.bgcolor,
            command= main_action.mnu_campania,
            font=general_style.f10,                
            label="Campaña",
            state="disabled"
        )
        self.menubar.add_command(
            background=general_style.bgcolor,
            command= main_action.mnu_salir,
            font=general_style.f10,                
            label="Salir"
        )

    def init(self):
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        self.top.geometry("550x250+%d+%d" % (screen_width/2-275, screen_height/2-125))
        
        self.top.resizable(0, 0)
        self.top.title("Tablero principal")
        self.top.configure(background=general_style.bgcolor)        
        self.top.state('zoomed')        
        self.makeMenu()
        session(self.top).init()

if __name__ == '__main__':
    vp_start_gui()





