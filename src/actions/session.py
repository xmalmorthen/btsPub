from controllers.dashboard import *

def btn_session_cancel():
    from libs import initWin
    initWin.destroy_window()

def btn_session_accept(self):
    from models import session as modelSession
    usr = modelSession.session().checkusr(usr = self.vUsuario.get(),pwd = self.vContrasenia.get())
    if usr == None:
        from tkinter import messagebox
        messagebox.showerror(message="Usuario y/o contraseña incorrecto", title="Inicio de session")
    else :
        self.fSesion.pack_forget()
        dashboard(self.top,usr[0][0]).init()
        