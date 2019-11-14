import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import assets.constants as constant
import assets.enums.messagesTypes as messagesTypesEnum
from assets.styles import general as general_style
from models import dashboardConfig, catalogs

class dashboard:    

    def __init__(self, top, idUsr = None):
        self.top = top
        self.__idUsr = idUsr
        self.__dashboardConfig = dashboardConfig.dashboardConfig()

    def __del__(self):
        self.__dashboardConfig.saveConfiguration(idUsr = self.__idUsr)

    def init(self):

        if not self.__idUsr:
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

        #frameConfigTop
        fConfigTop = tk.Frame(fConfig)
        fConfigTop.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fConfigTop.pack(fill = 'x')

        #framePaís
        f = tk.Frame(fConfigTop)
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
            values = self.__dashboardConfig.paisList
        )
        self.TCmbPais.current(0)
        self.TCmbPais_change(None)
        #/cmbPaís
        #/framePaís
        
        #frameCarrier
        f = tk.Frame(fConfigTop)
        f.configure(relief='flat',background= general_style.bgcolor)
        f.pack(side = 'left', padx=5, pady=5)
        #lblCarrier
        lbl = tk.Label(f)
        lbl.configure(
            background= general_style.bgcolor,
            font= general_style.f20,            
            text="Compañía"
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
            values = self.__dashboardConfig.carrierList
        )
        #/cmbCarrier
        #/frameCarrier

        #framePotencia
        f = tk.Frame(fConfigTop)
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
            sliderlength = 50,
            command = self.SclPotencia_Change
        )
        self.SclPotencia.set(10)
        #/sclPotencia
        #/framePotencia
        #/frameConfigTop

        #frameConfigBottom
        fConfigBottom = tk.Frame(fConfig)
        fConfigBottom.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fConfigBottom.pack(side= 'bottom', fill = 'x')

        #frameSaveConfig
        f = tk.Frame(fConfigBottom)
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
        #/frameConfigBottom
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
            width = 150,
            command= self.encenderApagar_click
        )
        self.btnEncenderApagar.image = img
        self.btnEncenderApagar.pack(fill='both', expand= True)
        #/#frameBtnEncenderApagar
        #/frameEstatus

        #FrameBitacora
        self.fTableroBitacora = tk.Frame(self.top)
        self.fTableroBitacora.configure(relief='groove',borderwidth="2",background= general_style.bgcolor)
        self.fTableroBitacora.pack(expand = True, fill = 'both')
        
        fTableroBitacoraHeader = tk.Frame(self.fTableroBitacora)
        fTableroBitacoraHeader.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fTableroBitacoraHeader.pack(fill = 'x')

        lbl = tk.Label(fTableroBitacoraHeader)
        lbl.configure(background= general_style.bgcolor,font= general_style.f20, text = 'Campañas')
        lbl.pack(side = 'left', padx = (5,0), pady = 5)

        lbl = tk.Label(self.fTableroBitacora)
        lbl.configure(background= general_style.bgcolor,font= general_style.f20, text = 'Bitácora')
        lbl.pack()

        self.bodyBitacora = tk.Frame(self.fTableroBitacora)
        self.bodyBitacora.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        self.bodyBitacora.pack(fill = 'both', expand=True)
        #/FrameBitacora

        self.fStatusBar = tk.Frame(self.top)
        self.fStatusBar.configure(relief='ridge',borderwidth="2",background= general_style.bgcolor)
        self.fStatusBar.pack(side= 'bottom', fill = 'x')

        if (self.retrieveInitConfig()):
            self.setStatusBarMsg(msg= 'Carga iniciada correctamente', msgType= messagesTypesEnum.type.INFO)

        self.populateGrid()

    def retrieveInitConfig(self):
        returnResponse = True
        import numpy as np
        response = self.__dashboardConfig.getConfiguration(self.__idUsr)
        if (len(response) > 0):
            for i in np.arange(len(self.__dashboardConfig.paisList)):
                if (self.__dashboardConfig.paisList[i].split('-')[0].strip() == str(response[0][2])):
                    self.TCmbPais.current(i)
                    self.TCmbPais_change(None)
                    break
            for i in np.arange(len(self.__dashboardConfig.carrierList)):
                if (self.__dashboardConfig.carrierList[i].split('-')[0].strip() == str(response[0][3])):
                    self.TCmbCarrier.current(i)
                    self.TCmbCarrier_change(None)
                    break
            self.SclPotencia.set(response[0][4])
            self.SclPotencia_Change(response[0][4])
            self.chkBtnAutoCnnVar.set(response[0][5])
            self.chkBtnAutoCnn_Click()
            returnResponse = self.encenderApagar_click()
            self.chkBtnConfigVar.set(1)
            self.chkBtnConfig_Click()
        return returnResponse

    def TCmbPais_change(self, event):
        if (self.TCmbPais.current() != -1):
            self.__dashboardConfig.paisValue = self.TCmbPais.get().split('-')[0].strip()

    def TCmbCarrier_change(self, event):
        if (self.TCmbCarrier.current() != -1):
            self.__dashboardConfig.carrierValue = self.TCmbCarrier.get().split('-')[0].strip()

    def SclPotencia_Change(self, value):
        self.__dashboardConfig.potencia = value

    def chkBtnAutoCnn_Click(self):
        self.__dashboardConfig.autoConnect = self.chkBtnAutoCnnVar.get()

    def chkBtnConfig_Click(self):
        self.__dashboardConfig.saveConfig = self.chkBtnConfigVar.get()        

    def encenderApagar_click(self):
        returnResponse = False
        try:
            if (self.TCmbPais.current() == -1):
                self.TCmbPais.focus()
                raise Exception('Debe seleccionar el país');
            if (self.TCmbCarrier.current() == -1):
                self.TCmbCarrier.focus()
                raise Exception('Debe seleccionar la compañía');
            if (self.SclPotencia.get() == 0):
                self.SclPotencia.focus()
                raise Exception('La potencia debe ser mayor a 0');

            self.__dashboardConfig.encenderApagar(parent = self)
            returnResponse = True
        except Exception as ex:
            self.setStatusBarMsg(msg= str(ex), msgType= messagesTypesEnum.type.ERROR, showMsgBox = True)
        return returnResponse

    def populateGrid(self):
        canvas = tk.Canvas(self.bodyBitacora, bg= general_style.bgcolor)
        canvas.pack(side = 'left', fill='both', expand = True)
        
        vsbar = tk.Scrollbar(self.bodyBitacora, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.pack(fill='y', side= 'right')
        canvas.configure( yscrollcommand=vsbar.set)

        # hsbar = tk.Scrollbar(self.bodyBitacora, orient=tk.HORIZONTAL, command=canvas.xview)
        # hsbar.pack(fill='x', side= 'bottom')
        # canvas.configure(xscrollcommand=hsbar.set)

        grid = tk.Frame(canvas)
        grid.configure(relief='flat',borderwidth="0",background= general_style.bgcolor )

        response = catalogs.tblBitacora().get()
        
        items = []
        for item in response:
            arrayCol = []
            for idx in range(0,len(item) -1):                
                arrayCol.append(item[idx])
            arrayCol.append('insert button')           
            items.append(arrayCol)

        items.insert(0,('Fecha','Hora','Registros','Mensajes','Campaña',''))

        odd = True
        for item in items:
            fra = tk.Frame(grid)

            backColor = '#eaeaea' if odd else general_style.bgcolor
            odd = not odd

            fra.configure(relief= tk.FLAT,borderwidth="0",background= backColor)
            fra.pack(fill = 'x')
            for col in item:
                lbl = tk.Label(fra, justify= tk.LEFT, width= (canvas.winfo_width() % 6))
                lbl.configure(relief= tk.FLAT, borderwidth= 0, background= backColor,font= general_style.f10, text = col)
                lbl.pack(side='left', fill='x', expand= True)
                lbl.bind("<ButtonPress-1>", lambda event: canvas.focus_set())
        
        
        win = canvas.create_window((0,0), window=grid, anchor=tk.NW)
        grid.update_idletasks()
        bbox = canvas.bbox(tk.ALL)        

        canvas.configure(scrollregion=bbox)
        canvas.itemconfigure(win,width = canvas.winfo_width())
        
        canvas.bind("<Up>",    lambda event: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Down>",  lambda event: canvas.yview_scroll( 1, "units"))
        canvas.focus_set()

        canvas.bind("<ButtonPress-1>", lambda event: canvas.focus_set())
        vsbar.bind("<ButtonPress-1>", lambda event: canvas.focus_set())

    def setStatusBarMsg(self, msg, msgType = messagesTypesEnum.type.INFO, showMsgBox = False):
        for widget in self.fStatusBar.winfo_children():
            widget.pack_forget()
        
        icon = 'msgTypeInfo24x24.png'
        if (msgType == messagesTypesEnum.type.WARNING):
            icon = 'msgTypeWarning24x24.png'
        elif (msgType == messagesTypesEnum.type.ERROR):
            icon = 'msgTypeError24x24.png'

        fraContainer = tk.Frame(self.fStatusBar)
        fraContainer.configure(relief='flat',borderwidth="2",background= general_style.bgcolor)
        fraContainer.pack(side= 'left', expand= True, fill = 'x')

        img = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + icon))
        lbl = tk.Label(fraContainer,image=img)
        lbl.image = img
        lbl.configure(background= general_style.bgcolor)
        lbl.pack(side='left',padx=(10,1), pady=5)

        lbl = tk.Label(fraContainer)
        lbl.configure(background= general_style.bgcolor,font= general_style.f15,text=msg)
        lbl.pack(side='left',pady=5)

        if (showMsgBox):
            if (msgType == messagesTypesEnum.type.WARNING):
                messagebox.showwarning(message=msg, title="Atención")
            elif (msgType == messagesTypesEnum.type.ERROR):
                messagebox.showerror(message=msg, title="Error")
            elif (msgType == messagesTypesEnum.type.INFO):
                messagebox.showinfo(message=msg, title="Aviso")
