from Substrato import *

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Módulo para el objeto substrato A
"""

class A(Substrato):

    def __init__(self): #Constructor del objeto
        super().__init__()
        self.nombre = ("A")

    def producirOtrasBiomoleculas(self, option, usos, count_cycles):
        """
        Función que elegirá qué biomolécula se produce (o en qué se transforma el Substrato) a partir de una opción
        :param option:
        :param usos:
        :return:
        """
        super().producirOtrasBiomoleculas()
        if option == "B":
            return self.producirB()
        elif option == "Beta":
            return self.producirBeta(usos, count_cycles)

    def producirB(self):
        """
        Función que simplemente regresa un objeto substrato B
        :return:
        """
        from B import B
        producto = B()
        return producto

    def producirBeta(self, usos, count_cycles):
        """
        Función que devuelve un objeto enzimático Beta con usos dados por el parámetro usos
        :param usos:
        :return:
        """
        from Beta import Beta
        producto = Beta(usos, count_cycles)
        return producto
