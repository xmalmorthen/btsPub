import tkinter as tk
from PIL import ImageTk, Image
import assets.constants as constant
from assets.styles import general as general_style
import actions.session as session_action

class session:
    def __init__(self, top):
        self.top = top
    
    def init(self):
        self.fSesion = tk.Frame(self.top)

        self.fSesion.configure(
            relief='groove',
            borderwidth="2",
            background= general_style.bgcolor,
            takefocus="1",
            width="635", 
            height="265"
        )
        self.fSesion.pack(expand=True)
        
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

        img_loginImage = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "loginImage64x64.png"))
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
        
        img_accept = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "accept64x64.png"))
        self.btnEntrar = tk.Button(self.fSesion, image=img_accept)
        self.btnEntrar.configure(            
            relief="groove",            
            background=general_style.bgcolor,
            font=general_style.f10,
            compound='top',
            text="Entrar",
            cursor= 'hand2',
            command=lambda: session_action.btn_session_accept(self),
        )
        self.btnEntrar.image = img_accept
        self.btnEntrar.place(relx=0.551, rely=0.491, height=118, width=129)

        img_cancel = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "cancel64x64.png"))
        self.btnCancelar = tk.Button(self.fSesion, image=img_cancel)
        self.btnCancelar.configure(            
            relief="groove",            
            background=general_style.bgcolor,
            font=general_style.f10,
            compound='top',
            text="Cancelar",
            cursor= 'hand2',
            command= session_action.btn_session_cancel,
        )
        self.btnCancelar.image = img_cancel
        self.btnCancelar.place(relx=0.772, rely=0.491, height=118, width=129)

        self.eUsuario.insert(0, 'xmalmorthen')
        self.eContrasenia.insert(0, '..121212qw')