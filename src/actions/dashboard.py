import tkinter as tk

def mnu_tablero():
    return None

def mnu_campania():
    return None

def mnu_salir():
    from libs import initWin
    initWin.destroy_window()

def btn_session_cancel():
    from libs import initWin
    initWin.destroy_window()

def btn_session_accept(usr,pwd):
    global __session__
    if usr == "xmalmorthen" and pwd == "..121212qw":
        __session__ = True
    else:
        __session__ = False
        from tkinter import messagebox
        messagebox.showinfo(message="Error", title="Inicio de session")