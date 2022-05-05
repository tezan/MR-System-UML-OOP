from Biomolecula import *

class Enzima(Biomolecula):
    count = 0

    def __init__(self, reusos):
        self.limiteDeVida = reusos
        self.degradado = False

    def catalizarSubstrato(self, Comida):
        pass

    def getStatusDegradacion(self):
        return self.degradado

    def __autodestruccion(self):
        print("Autodestrucción")
        self.degradado = True

    def registrarUso(self):
        self.__incrementarUsos()

    def __incrementarUsos(self):
        print("Desgastando...")
        self.limiteDeVida = self.limiteDeVida-1
        if self.limiteDeVida <= 0:
            self.__autodestruccion()



