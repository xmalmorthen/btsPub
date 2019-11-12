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

    def encenderApagar_click (self, parent):

        if self.estatus == 0:
            self.estatus = 1
            img = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOn64x64.png"))
            parent.lblEncendidoApagadoIcon.configure(image=img)
            parent.lblEncendidoApagadoIcon.image = img
            parent.lblEncendidoApagadoText['text'] = "Encendido"
        else:
            self.estatus = 0
            img = ImageTk.PhotoImage(Image.open( constant.IMAGESDIR + "bulbOff64x64.png"))
            parent.lblEncendidoApagadoIcon.configure(image=img)
            parent.lblEncendidoApagadoIcon.image = img
            parent.lblEncendidoApagadoText['text'] = "Apagado"

    def saveConfiguration(self, idUsr = None) :
        if idUsr != None:
            if self.saveConfig == 1:
                cat.caConfigUsr().put(idUser = idUsr, idPais = self.paisValue, idCarrier = self.carrierValue, potencia = self.potencia, autoConnect = self.autoConnect)
            else:
                cat.caConfigUsr().delete(idUsr)