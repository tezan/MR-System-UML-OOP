from Substrato import *

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Módulo para el objeto substrato B
"""

class B(Substrato):

    def __init__(self): #Constructor del objeto
        super().__init__()
        self.nombre = ("B")

    def producirOtrasBiomoleculas(self, option, usos, count_cycles):
        """
        Función que elegirá qué biomolécula se produce (o en qué se transforma el Substrato) a partir de una opción
        :param option:
        :param usos:
        :return:
        """
        super().producirOtrasBiomoleculas() #Delegado de responsabilidad a la clase parental
        if option == "F":
            return self.producirF()
        elif option == "FPrima":
            return self.producirFPrima(usos, count_cycles)

    def producirF(self):
        """
        Función que simplemente regresa un objeto substrato F
        :return:
        """
        from F import F
        producto = F()
        return producto

    def producirFPrima(self, usos, count_cycles):
        """
        Función que devuelve un objeto enzimático FPrima con usos dados por el parámetro usos
        :param usos:
        :return:
        """
        from FPrima import FPrima
        producto = FPrima(usos, count_cycles)
        return producto