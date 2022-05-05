from Enzima import *
import Substrato
import random as rand

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Módulo para el objeto enzimático Phi
"""

class Phi(Enzima):

    def __init__(self, reusos, count_cycles): #Constructor del objeto
        super().__init__(reusos)
        self.nombre = ("Phi " + str(count_cycles))

    def catalizarSubstrato(self, ambienteEnzimaticoOrigen: [Enzima], ambienteEnzimaticoDestino: [Enzima], ambienteSubstrato: [Substrato], ambienteSubstratoNuevo: [Substrato], count_cycles):
        """
        Función del catalizador Phi. Devuelve el ambiente celular completo que se ingresó.
        :param ambienteEnzimaticoOrigen:
        :param ambienteEnzimaticoDestino:
        :param ambienteSubstrato:
        :param ambienteSubstratoNuevo:
        :return:
        """
        super().catalizarSubstrato("B") #Delegado de responsabilidad a la clase parental
        elector = rand.choices((True, False, None), [0.4, 0.4, 0.2]) #Elegimos aleatoriamente True, False o None.
        ComidaB = ambienteSubstrato.pop() #Obtenemos un substrato-comida B para trabajar, el cual no volverá al ambiente
        eleccionAleatoria = elector.pop() #Obtenemos el valor de nuestra elección aleatoria
        #if eleccionAleatoria == None: #Si la elección aleatoria es None simulamos que la enzima no pudo hacer su trabajo
         #   print("No me pude acoplar...")
          #  return (ambienteEnzimaticoOrigen,ambienteEnzimaticoDestino, ambienteSubstrato, ambienteSubstratoNuevo)  #Regresamos lo que fue ingresado, tal cual.
        if True: #Caso para garantizar que siempre se realice catálisis para F
        #elif eleccionAleatoria == True: #Si la elección es True, catalizamos para F
            print("Phi: B -> F")
            producto = self.catalizarReparacionF(ComidaB)
            ambienteSubstratoNuevo.append(producto) #Agregamos el resultado de la catálisis al ambiente destino
        if True: #Caso para garantizar que siempre se realice catálisis para FPrima
        #elif eleccionAleatoria == False: #Si la elección es False, catalizamos para FPrima
            print("Phi: B -> FPrima")
            producto = self.catalizarReparacionFPrima(ComidaB, count_cycles)
            ambienteEnzimaticoDestino.append(producto) #Agregamos el resultado de la catálisis al ambiente destino
        if self.getStatusDegradacion() == True: #Si la enzima no está biodisponible
            print("Esta Phi se ha degradado y no será devuelta al ambiente.")
        elif self.getStatusDegradacion() == False:
            print("Devolviendo")
            ambienteEnzimaticoOrigen.append(self) #Si llegmos hasta acá, regresamos la enzima Phi al ambiente
        return (ambienteEnzimaticoOrigen,ambienteEnzimaticoDestino, ambienteSubstrato, ambienteSubstratoNuevo) #Devolvemos los ambientes alterados

    def catalizarReparacionF(self, b):
        """
        Función de catálisis específica para el producto F y con substrato B
        :param b:
        :return:
        """
        produccion = b.producirOtrasBiomoleculas("F", 3, 0)  #Asignamos a producción lo que produzca el substrato B al ser catalizado con la opción F y un parámetro dummy.
        self.registrarUso() #Aumentamos el conteo de usos de la enzima Phi por uno.
        return produccion  #Regresamos el producto

    def catalizarReparacionFPrima(self, b, count_cycles):
        """
        Función de catálisis específica para el producto FPrima y con substrato B
        :param b:
        :return:
        """
        #usos = rand.randint(1, 5) #Construimos los usos que tendrá la enzima de manera aleatoria
        usos = 1 #Construimos los usos según Zhang et al. (2016)
        produccion = b.producirOtrasBiomoleculas("FPrima", usos, count_cycles) #Asignamos a producción lo que produzca el substrato B al ser catalizado con la opción FPrima y un parámetro de usos.
        print("Registrando uso")
        self.registrarUso() #Aumentamos el conteo de usos de la enzima Phi por uno.
        return produccion #Regresamos el producto