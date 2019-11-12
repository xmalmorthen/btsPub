import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import assets.constants as constant
from assets.styles import general as general_style
from models import dashboardConfig

class dashboard:    

    def __init__(self, top, idUsr = None):
        self.top = top
        self.idUsr = idUsr
        self.dashboardConfig = dashboardConfig.dashboardConfig()

    def __del__(self):
        self.dashboardConfig.saveConfiguration(idUsr = self.idUsr)

    def init(self):

        if not self.idUsr:
            messagebox.showerror(message="Acceso denegado", title="Tablero principal")
            return None

        for widget in self.top.winfo_children():
            if isinstance(widget, tk.Menu):
                self.menubar = widget
                break
                
        self.menubar.entryconfig("Tablero", state="normal")
        self.menubar.entryconfig("Campaña", state="normal")

        #frameheader
        fHeader = tk.Frame(self.top)
        fHeader.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fHeader.pack(fill = 'both',padx=5, pady=5)

        #frame configuraciones
        fConfig = tk.Frame(fHeader)
        fConfig.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fConfig.pack(side = 'left', fill = 'x')

        #framePaís
        f = tk.Frame(fConfig)
        f.configure(relief='flat',background= general_style.bgcolor)
        f.pack(side = 'left',padx=5, pady=5)

        #lblPaís
        lbl = tk.Label(f)
        lbl.configure(
            background= general_style.bgcolor,            
            font= general_style.f20,
            anchor='w',
            text="País"
        )
        lbl.pack()
        #/lblPaís
        #cmbPaís
        self.TCmbPais = ttk.Combobox(f, state="readonly")
        self.TCmbPais.pack(side='bottom')
        self.TCmbPais.bind("<<ComboboxSelected>>", self.TCmbPais_change)
        self.TCmbPais.configure(
            cursor ="fleur",
            font = general_style.f20,
            values = self.dashboardConfig.paisList
        )
        self.TCmbPais.current(0)
        #/cmbPaís
        #/framePaís
        
        #frameCarrier
        f = tk.Frame(fConfig)
        f.configure(relief='flat',background= general_style.bgcolor)
        f.pack(side = 'left', padx=5, pady=5)
        #lblCarrier
        lbl = tk.Label(f)
        lbl.configure(
            background= general_style.bgcolor,
            font= general_style.f20,            
            text="Carrier"
        )
        lbl.pack()
        #/lblCarrier
        #cmbCarrier
        
        self.TCmbCarrier = ttk.Combobox(f,state="readonly")
        self.TCmbCarrier.pack(side='bottom')
        self.TCmbCarrier.bind("<<ComboboxSelected>>", self.TCmbCarrier_change)
        self.TCmbCarrier.configure(
            background= general_style.bgcolor,
            cursor ="fleur",
            font = general_style.f20,
            values = self.dashboardConfig.carrierList
        )
        #/cmbCarrier
        #/frameCarrier

        #framePotencia
        f = tk.Frame(fConfig)
        f.configure(relief='flat',background= general_style.bgcolor)
        f.pack(side = 'left', padx=5, pady=5)
        #lblPotencia
        lbl = tk.Label(f)
        lbl.configure(
            background= general_style.bgcolor,
            font= general_style.f20,            
            text="Potencia"
        )
        lbl.pack()
        #/lblPotencia
        #sclPotencia
        self.SclPotencia = tk.Scale(f, from_=1.0, to=20.0)
        self.SclPotencia.pack(side = 'bottom' )
        self.SclPotencia.configure(
            orient="horizontal",
            sliderrelief="ridge",            
            background= 'white',
            font= general_style.f10,
            length="332",
            sliderlength = 50
        )
        self.SclPotencia.set(10)
        #/sclPotencia
        #/framePotencia
        #/frame configuraciones

        #frameEstatus
        fEstatus = tk.Frame(fHeader)
        fEstatus.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fEstatus.pack(side = 'right', padx=5, pady=5, fill = 'both')
        
        #frameEstatusIcon
        f = tk.Frame(fEstatus)
        f.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        f.pack(side = 'left', padx=5)

        lbl = tk.Label(f)
        lbl.configure(
            background= general_style.bgcolor,            
            font= general_style.f10,
            text="Estatus"
        )
        lbl.pack()
        
        img = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOff64x64.png"))
        self.lblEncendidoApagadoIcon = tk.Label(f,image=img)
        self.lblEncendidoApagadoIcon.image = img
        self.lblEncendidoApagadoIcon.configure(
            background= general_style.bgcolor,            
            font= general_style.f20            
        )        
        self.lblEncendidoApagadoIcon.pack()
        
        self.lblEncendidoApagadoText = tk.Label(f)
        self.lblEncendidoApagadoText.image = img
        self.lblEncendidoApagadoText.configure(
            background= general_style.bgcolor,
            font= general_style.f10,
            text="Apagado"
        )        
        self.lblEncendidoApagadoText.pack()
        #/frameEstatusIcon

        #frameBtnEncenderApagar
        f = tk.Frame(fEstatus)
        f.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        f.pack(side = 'right', fill='both' , padx=5)

        img = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOn64x64.png"))
        self.btnEncenderApagar = tk.Button(f, image=img)
        self.btnEncenderApagar.configure(            
            relief="groove",
            background=general_style.bgcolor,
            font=general_style.f10,
            compound='top',
            text="Encender",
            cursor= 'hand2',
            command= lambda: self.dashboardConfig.encenderApagar_click(parent = self)
        )
        self.btnEncenderApagar.image = img
        self.btnEncenderApagar.pack(fill='both', expand= True)
        #/#frameBtnEncenderApagar
        #/frameEstatus

        #frameSaveConfig
        f = tk.Frame(self.top)
        f.configure(relief='flat',background= general_style.bgcolor)
        f.pack(side= 'top', fill = 'x',padx=10, pady=5)

        #chkAutoCnn        
        self.chkBtnAutoCnn = tk.Checkbutton(f)
        self.chkBtnAutoCnn.pack(side='left')
        self.chkBtnAutoCnnVar = tk.IntVar()
        self.chkBtnAutoCnn.configure(
           background= general_style.bgcolor,
           justify='left',
           font= general_style.f10,
           text="Autoconectar al iniciar",
           variable = self.chkBtnAutoCnnVar,
           command = self.chkBtnAutoCnn_Click
        )
        #/chkAutoCnn

        #chkConfig
        self.chkBtnConfig = tk.Checkbutton(f)
        self.chkBtnConfig.pack(side='left',padx=15)
        self.chkBtnConfigVar = tk.IntVar()
        self.chkBtnConfig.configure(
           background= general_style.bgcolor,
           justify='left',
           font= general_style.f10,
           text="Guardar configuración",
           variable = self.chkBtnConfigVar,
           command = self.chkBtnConfig_Click
        )
        #/chkConfig
        #/frameSaveConfig

        self.fTableroBitacora = tk.Frame(self.top)
        self.fTableroBitacora.configure(relief='groove',borderwidth="2",background= '#cacaca',
        )
        self.fTableroBitacora.pack(expand = True, fill = 'both')

    def TCmbPais_change(self, event):
        self.dashboardConfig.paisValue = self.TCmbPais.get()

    def TCmbCarrier_change(self, event):
        self.dashboardConfig.carrierValue = self.TCmbCarrier.get()

    def chkBtnAutoCnn_Click(self):
        self.dashboardConfig.autoConnect = self.chkBtnAutoCnnVar.get()

    def chkBtnConfig_Click(self):
        self.dashboardConfig.saveConfig = self.chkBtnConfigVar.get()        
