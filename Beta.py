from Enzima import *
import Substrato
import random as rand

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Módulo para el objeto enzimático Beta
"""

class Beta(Enzima):

    def __init__(self, reusos, count_cycles): #Constructor del objeto
        super().__init__(reusos)
        self.nombre = ("Beta " + str(count_cycles))

    def catalizarSubstrato(self, ambienteEnzimaticoOrigen: [Enzima], ambienteEnzimaticoDestino: [Enzima], ambienteSubstrato: [Substrato], count_cycles):
        """
        Función del catalizador Beta. Devuelve el ambiente celular completo que se ingresó.
        :param ambienteEnzimaticoOrigen:
        :param ambienteEnzimaticoDestino:
        :param ambienteSubstrato:
        :return:
        """
        super().catalizarSubstrato("B") #Delegado de responsabilidad a la clase parental
        elector = rand.choices((True, False), [0.5, 0.5]) #Elegimos aleatoriamente True, False o None.
        ComidaF = ambienteSubstrato.pop() #Obtenemos un substrato-comida F para trabajar, el cual no volverá al ambiente
        eleccionAleatoria = elector.pop() #Obtenemos el valor de nuestra elección aleatoria
        #if eleccionAleatoria == False: #Si la elección aleatoria es False simulamos que la enzima no pudo hacer su trabajo
         #   print("No me pude acoplar...")
          #  return (ambienteEnzimaticoOrigen,ambienteEnzimaticoDestino, ambienteSubstrato)  #Regresamos lo que fue ingresado, tal cual.
        if True: #Caso para garantizar que siempre se realice catálisis para FPrima
        #elif eleccionAleatoria == True: #Si la elección es True, catalizamos para Phi
            print("Beta: F -> Phi")
            producto = self.catalizarReplicacion(ComidaF, count_cycles)
            ambienteEnzimaticoDestino.append(producto) #Agregamos el resultado de la catálisis al ambiente destino
        if self.getStatusDegradacion() == True: #Si la enzima no está biodisponible
            print("Esta Beta se ha degradado y no será devuelta al ambiente.")
        elif self.getStatusDegradacion() == False:
            print("Devolviendo")
            ambienteEnzimaticoOrigen.append(self) #Si llegmos hasta acá, regresamos la enzima Beta al ambiente
        return (ambienteEnzimaticoOrigen,ambienteEnzimaticoDestino, ambienteSubstrato) #Devolvemos los ambientes alterados

    def catalizarReplicacion(self, f, count_cycles):
        """
        Función de catálisis específica para el producto Phi y con substrato F
        :param f:
        :return:
        """
        #usos = rand.randint(1, 5) #Construimos los usos que tendrá la enzima de manera aleatoria
        usos = 1 #Construimos los usos según Zhang et al. (2016)
        produccion = f.producirOtrasBiomoleculas(usos,count_cycles) #Asignamos a producción lo que produzca el substrato B al ser catalizado con la opción FPrima y un parámetro de usos.
        print("Registrando uso")
        self.registrarUso() #Aumentamos el conteo de usos de la enzima Phi por uno.
        return produccion #Regresamos el producto