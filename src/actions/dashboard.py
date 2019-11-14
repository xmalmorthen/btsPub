class action(object):

    __instance = None

    isConnected = False

    def __new__(cls):
        if action.__instance is None:
            action.__instance = object.__new__(cls)
        return action.__instance

    def connect(self):
        returnResult = False
        #TODO: Implementar los comados de conexión

        self.isConnected = returnResult;
        return returnResult

    def disconect(self):
        returnResult = False
        #TODO: Implementar los comados de desconexión
        self.isConnected = returnResult;
        return returnResult