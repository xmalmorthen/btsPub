import os
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from libs import initWin
from assets.styles import general as general_style
import actions.dashboard as dashboard_action

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    #btsPubMain.set_Tk_var()
    top = dashboard (root)
    initWin.init(root, top)
    root.mainloop()

class dashboard:

    app_carpeta = os.getcwd()
    img_carpeta = app_carpeta + os.sep + "src" + os.sep + "assets" + os.sep + "images"
    
    def __init__(self, top=None):        
                        
        top.resizable(0, 0)
        top.title("Tablero principal")
        top.configure(background=general_style.bgcolor)        
        top.state('zoomed')

        self.menubar = tk.Menu(
            top,
            font = general_style.f10,
            bg = general_style.bgcolor,
            fg = general_style.fgcolor
        )
        top.configure(menu = self.menubar)

        self.menubar.add_command(
            background=general_style.bgcolor,
            command= dashboard_action.mnu_tablero,
            font=general_style.f10,
            label="Tablero",
            state="disabled"
        )
        self.menubar.add_command(
            background=general_style.bgcolor,
            command= dashboard_action.mnu_campania,
            font=general_style.f10,                
            label="Campaña",
            state="disabled"
        )
        self.menubar.add_command(
            background=general_style.bgcolor,
            command= dashboard_action.mnu_salir,
            font=general_style.f10,                
            label="Salir"
        )

        # self.fTablero = tk.Frame(top)
        # self.fTablero.place(
        #     relx=0.017, 
        #     rely=0.017, 
        #     relheight=0.967,
        #     relwidth=0.975
        # )
        # self.fTablero.configure(
        #     relief='groove',
        #     borderwidth="2",
        #     background="#d9d9d9",
        #     highlightbackground="#d9d9d9",
        #     highlightcolor="black"
        # )        
        # self.fTablero.place_forget()

        self.fSesion = tk.Frame(top)

        self.fSesion.configure(
            relief='groove',
            borderwidth="2",
            background= general_style.bgcolor,
            takefocus="1",
            width="635", 
            height="265"
        )
        self.fSesion.pack(expand=True)
        #self.fSesion.pack_forget() #ocultar frame
        
        self.lblUsr = tk.Label(self.fSesion)
        self.lblUsr.configure(
            background= general_style.bgcolor,            
            font= general_style.f20,            
            text="Usuario"
        )
        self.lblUsr.place(relx=0.02, rely=0.34, height=43, width=105)

        self.lblContrasenia = tk.Label(self.fSesion)
        self.lblContrasenia.configure(
            background= general_style.bgcolor,            
            font= general_style.f20,            
            text="Contraseña"
        )        
        self.lblContrasenia.place(relx=0.011, rely=0.642, height=43, width=165)

        self.eUsuario = tk.Entry(self.fSesion)
        self.vUsuario = tk.StringVar()
        self.eUsuario.configure(
            background="white",
            font= general_style.f20,
            relief="groove",
            textvariable= self.vUsuario,
        )
        self.eUsuario.place(relx=0.027, rely=0.491,height=35, relwidth=0.51)
        self.eUsuario.focus()

        self.eContrasenia = tk.Entry(self.fSesion)
        self.vContrasenia = tk.StringVar()
        self.eContrasenia.configure(
            background="white",
            font= general_style.f20,
            relief="groove",
            show="*",
            textvariable= self.vContrasenia,
        )
        self.eContrasenia.place(relx=0.027, rely=0.796, height=35, relwidth=0.51)

        img_loginImage = ImageTk.PhotoImage(Image.open( self.img_carpeta + os.sep + "loginImage64x64.png"))
        self.lblImageSesion = tk.Label(self.fSesion, image=img_loginImage)
        self.lblImageSesion.image = img_loginImage
        self.lblImageSesion.configure(background= general_style.bgcolor)
        self.lblImageSesion.place(relx=0.031, rely=0.095, height=64, width=64)

        self.lblTitle = tk.Label(self.fSesion)        
        self.lblTitle.configure(
            background=general_style.bgcolor,
            font=general_style.TitleLg,
            justify='left',
            text='''Iniciar sesión''',
        )
        self.lblTitle.place(relx=0.137, rely=0.038, height=73, width=405)
        
        img_accept = ImageTk.PhotoImage(Image.open( self.img_carpeta + os.sep + "accept64x64.png"))
        self.btnEntrar = tk.Button(self.fSesion, image=img_accept)
        self.btnEntrar.configure(            
            relief="groove",            
            background=general_style.bgcolor,
            font=general_style.f10,
            compound='top',
            text="Entrar",
            command=lambda: dashboard_action.btn_session_accept(usr = self.vUsuario.get(), pwd = self.vContrasenia.get()),
        )
        self.btnEntrar.image = img_accept
        self.btnEntrar.place(relx=0.551, rely=0.491, height=118, width=129)

        img_cancel = ImageTk.PhotoImage(Image.open( self.img_carpeta + os.sep + "cancel64x64.png"))
        self.btnCancelar = tk.Button(self.fSesion, image=img_cancel)
        self.btnCancelar.configure(            
            relief="groove",            
            background=general_style.bgcolor,
            font=general_style.f10,
            compound='top',
            text="Cancelar",
            command= dashboard_action.btn_session_cancel,
        )
        self.btnCancelar.image = img_cancel
        self.btnCancelar.place(relx=0.772, rely=0.491, height=118, width=129)


if __name__ == '__main__':
    vp_start_gui()





