from PIL import ImageTk, Image
from models import catalogs as cat
import assets.constants as constant

class dashboardConfig:
    carrierList = None
    paisList = None

    paisValue = -1
    carrierValue = -1
    potencia = 10

    estatus = 0

    autoConnect = 0
    saveConfig = 0

    def __init__ (self):
        self.carrierList = []
        for carrier in cat.carriers().get(catalog = 'caCarriers',where = 'active == 1'):
            self.carrierList.append(str(carrier[0]) + " - " + str(carrier[3]))
        self.paisList = []
        for pais in cat.pais().get(catalog = 'caPaises',where = 'active == 1'):
            self.paisList.append(str(pais[0]) + " - " + str(pais[3]))  

    def encenderApagar(self, parent):
        returnResponse = None
        imgLbl = None
        imgBtn = None
        textLbl = ''
        textBtn = ''
        lblIcon = parent.lblEncendidoApagadoIcon
        lblText = parent.lblEncendidoApagadoText
        btn = parent.btnEncenderApagar

        import actions.dashboard as dashboard

        dashboardAction = dashboard.action()

        if self.estatus == 0:
            if (dashboardAction.isConnected == False):
                if (not dashboardAction.connect()):
                    raise Exception('No se pudo conectar')

            self.estatus = 1
            imgLbl = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOn64x64.png"))
            imgBtn = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOff64x64.png"))
            textLbl = 'Encendido'
            textBtn = 'Apagar'
        else:

            if (dashboardAction.isConnected):
                if (not dashboardAction.disconect()):
                    raise Exception('No se pudo desconectar')

            self.estatus = 0
            imgLbl = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOff64x64.png"))
            imgBtn = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOn64x64.png"))
            textLbl = 'Apagado'
            textBtn = 'Encender'
        
        lblIcon.configure(image=imgLbl)
        lblIcon.image = imgLbl
        lblText['text'] = textLbl
        btn.configure(image=imgBtn, text=textBtn)
        btn.image = imgBtn
        
        return returnResponse

    def saveConfiguration(self, idUsr = None) :
        if idUsr != None:
            if self.saveConfig == 1:
                cat.caConfigUsr().put(idUser = idUsr, idPais = self.paisValue, idCarrier = self.carrierValue, potencia = self.potencia, autoConnect = self.autoConnect)
            else:
                cat.caConfigUsr().delete(idUsr)
    
    def getConfiguration(self, idUsr = None):
        returnResult = None
        if idUsr != None:
            returnResult = cat.caConfigUsr().get(idUser = idUsr)
        return returnResult