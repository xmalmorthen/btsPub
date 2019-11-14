import sqlite3
from datetime import datetime

class base:
    
    def __init__(self):
        self.__cnn = sqlite3.connect("btsPubEntities.db")
        self.__cur = self.cnn.cursor()
        self.__now = datetime.now()

    def __del__(self):
        self.__cnn.close()

    @property
    def cnn(self):
        return self.__cnn

    @property
    def cur(self):
        return self.__cur

    @property
    def now(self):
        return self.__now

    def get(self, catalog, where = None):
        returnResult = None

        qry = "SELECT * FROM " + catalog

        if where != None:
            qry += " WHERE " + where

        self.cur.execute(qry)

        returnResult = self.cur.fetchall()

        return returnResult

class carriers(base):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

class pais(base):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

class caConfigUsr(base):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def get(self,idUser):
        return super().get(catalog = 'caConfigUsr', where = "idUser = " + str(idUser)) 

    def put(self,idUser, idPais, idCarrier, potencia, autoConnect):
        returnResult = False

        try:
            if self.delete(idUser = idUser):
                qry = "INSERT INTO caConfigUsr(idUser,idPais,idCarrier,potencia,autoConnect,fIns) VALUES(?,?,?,?,?,?)"
                self.cur.executemany(qry,[(idUser, idPais, idCarrier, potencia, autoConnect, self.now.strftime("%Y/%m/%d, %H:%M:%S"))])
                self.cnn.commit()
                returnResult = True
        except Exception as ex:
            print (ex)
            returnResult = False

        return returnResult

    def delete(self,idUser):
        returnResult = False

        try:
            qry = "DELETE FROM caConfigUsr WHERE idUser = " + str(idUser)
            self.cur.execute(qry)
            self.cnn.commit()
            returnResult = True
        except Exception as ex:
            print (ex)
            returnResult = False

        return returnResult

class tblBitacora(base):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def get(self,filter = None):
        returnResult = None

        qry = "SELECT * FROM vwBitacora"
        if filter != None:
           qry += " where " + filter 

        self.cur.execute(qry)
        returnResult = self.cur.fetchall()
        
        return returnResult