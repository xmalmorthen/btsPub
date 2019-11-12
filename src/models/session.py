import sqlite3

class session:
    def __init__(self):
        self.cnn = sqlite3.connect("btsPubEntities.db")
        self.cur = self.cnn.cursor()

    def __del__(self):
        self.cnn.close()

    def checkusr(self, usr, pwd):
        returnResult = None

        qry = "SELECT id FROM caUsers WHERE userName = '" + usr + "' AND pwd = '" + pwd + "'"
        self.cur.execute(qry)

        usrDB = self.cur.fetchall()

        if len(usrDB) > 0:
            returnResult = usrDB

        return returnResult