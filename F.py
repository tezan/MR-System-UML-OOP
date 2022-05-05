from Substrato import *

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Módulo para el objeto substrato F
"""

class F(Substrato):

    def __init__(self): #Constructor del objeto
        super().__init__()
        self.nombre = ("F")

    def producirOtrasBiomoleculas(self, usos, count_cycles):
        """
        Función que solicitará al substrato producir/transformarse en un único tipo de biomolécula
        :param usos:
        :return:
        """
        super().producirOtrasBiomoleculas()
        return self.producirPhi(usos, count_cycles)

    def producirPhi(self,usos, count_cycles):
        """
        Función que devuelve un objeto enzimático Phi con usos dados por el parámetro usos
        :param usos:
        :return:
        """
        from Phi import Phi
        producto = Phi(usos, count_cycles)
        return producto


