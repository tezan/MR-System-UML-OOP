from Enzima import *
import Substrato
import random as rand

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Módulo para el objeto enzimático FPrima
"""

class FPrima(Enzima):

    def __init__(self, reusos, count_cycles): #Constructor del objeto
        super().__init__(reusos)
        self.nombre = ("FPrima " + str(count_cycles))

    def catalizarSubstrato(self, ambienteEnzimaticoOrigen: [Enzima], ambienteEnzimaticoDestino: [Enzima], ambienteSubstrato: [Substrato], ambienteSubstratoNuevo: [Substrato], count_cycles):
        """
        Función del catalizador FPrima. Devuelve el ambiente celular completo que se ingresó.
        :param ambienteEnzimaticoOrigen:
        :param ambienteEnzimaticoDestino:
        :param ambienteSubstrato:
        :param ambienteSubstratoNuevo:
        :return:
        """
        super().catalizarSubstrato("A") #Delegado de responsabilidad a la clase parental
        elector = rand.choices((True, False, None), [0.4, 0.4, 0.2]) #Elegimos aleatoriamente True, False o None.
        ComidaA = ambienteSubstrato.pop() #Obtenemos un substrato-comida B para trabajar, el cual no volverá al ambiente
        eleccionAleatoria = elector.pop() #Obtenemos el valor de nuestra elección aleatoria
        #if eleccionAleatoria == None: #Si la elección aleatoria es None simulamos que la enzima no pudo hacer su trabajo
         #   print("No me pude acoplar...")
          #  return (ambienteEnzimaticoOrigen, ambienteEnzimaticoDestino, ambienteSubstrato, ambienteSubstratoNuevo) #Regresamos lo que fue ingresado, tal cual.
        if True: #Caso para garantizar que siempre se realice catálisis para B
        #elif eleccionAleatoria == True: #Si la elección es True, catalizamos para B
            print("FPrima: A -> B")
            producto = self.catalizarMetabolismoB(ComidaA)
            ambienteSubstratoNuevo.append(producto)  #Agregamos el resultado de la catálisis al ambiente destino
        if True: #Caso para garantizar que siempre se realice catálisis para Beta
        #elif eleccionAleatoria == False: #Si la elección es False, catalizamos para Beta
            print("FPrima: A -> Beta")
            producto = self.catalizarMetabolismoBeta(ComidaA, count_cycles)
            ambienteEnzimaticoDestino.append(producto) #Agregamos el resultado de la catálisis al ambiente destino
        if self.getStatusDegradacion() == True: #Si la enzima no está biodisponible
            print("Esta FPrima se ha degradado y no será devuelta al ambiente.")
        elif self.getStatusDegradacion() == False:
            print("Devolviendo")
            ambienteEnzimaticoOrigen.append(self) #Si llegmos hasta acá, regresamos la enzima FPrima al ambiente
        return (ambienteEnzimaticoOrigen,ambienteEnzimaticoDestino, ambienteSubstrato, ambienteSubstratoNuevo) #Devolvemos los ambientes alterados

    def catalizarMetabolismoB(self, a):
        """
        Función de catálisis específica para el producto B y con substrato A
        :param a:
        :return:
        """
        produccion = a.producirOtrasBiomoleculas("B", 3, 0) #Asignamos a producción lo que produzca el substrato A al ser catalizado con la opción B y un parámetro dummy.
        self.registrarUso() #Aumentamos el conteo de usos de la enzima FPrima por uno
        return produccion  #Regresamos el producto

    def catalizarMetabolismoBeta(self, a, count_cycles):
        """
        Función de catálisis específica para el producto Beta y con substrato A
        :param a:
        :return:
        """
        #usos = rand.randint(1, 5) #Construimos los usos que tendrá la enzima de manera aleatoria
        usos = 1 #Construimos los usos según Zhang et al. (2016)
        produccion = a.producirOtrasBiomoleculas("Beta", usos, count_cycles) #Asignamos a producción lo que produzca el substrato A al ser catalizado con la opción Beta y un parámetro de usos.
        print("Registrando uso")
        self.registrarUso() #Aumentamos el conteo de usos de la enzima FPrima por uno
        return produccion #Regresamos el producto