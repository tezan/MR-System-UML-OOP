from A import A
from B import B
from F import F
from FPrima import FPrima
from Beta import Beta
from Phi import Phi

import numpy as np
import matplotlib.pyplot as plt
import random as rand
import os

"""
@Autor: Enrique Francisco Soto Astorga
@Versión: 1.0
@Descripción: Main para construir un ambiente celular y simular un Sistema-(M,R) según el diagrama UML de Zhang et al. (2016).
"""

def main():

    def count(start=0, step=1): #Función para aumentar un conteo, utilizada en la graficación
        n = start
        while True:
            yield n
            n += step

    plt.style.use('ggplot') #El estilo de gráfica
    x_vals = [] #Almacén de valores para eje X en la gráfica
    index = count() #Contador para aumentar valores en la gráfica

    def celula(): #Función que construye un ambiente celular y pone a trabajar al Sistema-(M,R)
        print("Construyendo ambiente celular...")
        #Ambientes para cada tipo de biomolécula
        Beta_environ = []
        Phi_environ = []
        FPrima_environ = []
        A_environ = []
        B_environ = []
        F_environ = []

        #Construcción de cada tipo de ambiente enzimático
        for i in range(3):
            #usos = rand.randint(1, 5) #Construimos los usos que tendrá la enzima de manera aleatoria
            FPrima_environ.append(FPrima(3, 0))
        for i in range(3):
            #usos = rand.randint(1, 5) #Construimos los usos que tendrá la enzima de manera aleatoria
            Beta_environ.append(Beta(3, 0))
        for i in range(3):
            #usos = rand.randint(1, 5) #Construimos los usos que tendrá la enzima de manera aleatoria
            Phi_environ.append(Phi(3, 0))
        #Construcción de cada tipo de ambiente de substratos
        for i in range(3):
            F_environ.append(F())
        for i in range(3):
            B_environ.append(B())
        for i in range(1):
            A_environ.append(A())

        count_cycles = 0 #Contador de ciclos para algunos experimentos
        count_veces_realimento = 0
        #Contadores de longitudes de cada ambiente, utilizados como output para graficar el comportamiento del Sistema-(M,R)
        count_FPrima = []
        count_Beta = []
        count_Phi = []
        count_A = []
        count_B = []
        count_F = []
        #Contadores de vida útil de cada enzima cuando no están en uso
        FPrima_counter = 0
        Beta_counter = 0
        Phi_counter = 0


        while True: #Inicio de la simulacións
            if count_cycles > 3000:
                break
            import Enzima
            print("Actual")
            print("|A| = "+str(len(A_environ))+", |B| = "+str(len(B_environ))+", |F| ="+str(len(F_environ)))
            print("|FPrima| = " + str(len(FPrima_environ)) + ", |Beta| = " + str(len(Beta_environ)) + ", |Phi| =" + str(len(Phi_environ)))
            
            FPrima_printer = []
            Phi_printer = []
            Beta_printer = []
            for i in range(len(FPrima_environ)):
                FPrima_printer.append(FPrima_environ[i].nombre)
            for i in range(len(Beta_environ)):
                Beta_printer.append(Beta_environ[i].nombre)
            for i in range(len(Phi_environ)):
                Phi_printer.append(Phi_environ[i].nombre)
            print("FPrima list:")
            print(FPrima_printer)
            print("Beta list:")
            print(Beta_printer)
            print("Phi list:")
            print(Phi_printer)

            if count_cycles<11000: #Si llevamos menos de n-ciclos, alimentar con A al Sistema-(M,R)
                A_environ.append(A())
            if len(FPrima_environ)<100 and count_veces_realimento<3:
                count_veces_realimento = count_veces_realimento+1
                while len(A_environ)<100:
                    A_environ.append(A())
            count_cycles = count_cycles+1 #Aumentar los cliclos por uno
            count_FPrima.append(len(FPrima_environ)) #Contar los FPrima
            count_Beta.append(len(Beta_environ)) #Contar los Beta
            count_Phi.append(len(Phi_environ)) #Contar los Phi
            count_A.append(len(A_environ)) #Contar los A
            count_B.append(len(B_environ)) #Contar los B
            count_F.append(len(F_environ)) #Contar los F
            x_vals.append(next(index))
            print("Ciclo:")
            print(count_cycles)
            if len(FPrima_environ)>0: #Si todavía hay enzimas FPrima
                if len(A_environ)>0: #Y hay comida para FPrima:
                    #FPrima: A -> B/Beta
                    enzima1 = FPrima_environ.pop(0) #Sacamos la FPrima y la usamos
                    FPrima_environ, Beta_environ, A_environ, B_environ = enzima1.catalizarSubstrato(FPrima_environ, Beta_environ, A_environ, B_environ, count_cycles)
            if len(Phi_environ)>0: #Si todavía hay enzimas Phi
                if len(B_environ)>0: #Y hay comida para Phi:
                    #Phi: B -> F/FPrima
                    enzima2 = Phi_environ.pop(0) #Sacamos la Phi y la usamos
                    Phi_environ, FPrima_environ, B_environ, F_environ = enzima2.catalizarSubstrato(Phi_environ, FPrima_environ, B_environ, F_environ, count_cycles)
            if len(Beta_environ)>0: #Si todavía hay enzimas Beta
                if len(F_environ)>0 : #Y hay comida para Beta:
                    #Beta: F -> Phi
                    enzima3 = Beta_environ.pop(0) #Sacamos la Beta y la usamos
                    Beta_environ, Phi_environ, F_environ = enzima3.catalizarSubstrato(Beta_environ, Phi_environ, F_environ, count_cycles)
            #if F_environ ==  [] and B_environ == [] and A_environ == []: #Si ya no hay comida, detenemos la simulación
             #   break
            if len(FPrima_environ) == 0 and len(Beta_environ) == 0 and len(Phi_environ) == 0: #Si ya no hay enzimas, detenemos la simulación.
                break
            if len(FPrima_environ) > 0: #Si hay FPrimas
                if FPrima_counter < 3: #Y el contador de vida útil no se ha rebasado
                    FPrima_counter = FPrima_counter+1 #Aumentar el contador
                if FPrima_counter == 3: #Si el contador está por rebasarse
                    FPrima_counter = 0 #Se reinicia
                    FPrima_environ.pop() #Sacamos una FPrima
            if len(Beta_environ) > 0: #Si hay Betas
                if Beta_counter < 3: #Y el contador de vida útil no se ha rebasado
                    Beta_counter = Beta_counter+1 #Aumentar el contador
                if Beta_counter == 3: #Si el contador está por rebasarse
                    Beta_counter = 0 #Se reinicia
                    Beta_environ.pop() #Sacamos una Beta
            if len(Phi_environ) > 0: #Si hay Phis
                if Phi_counter < 3: #Y el contador de vida útil no se ha rebasado
                    Phi_counter = Phi_counter+1 #Aumentar el contador
                if Phi_counter == 3: #Si el contador está por rebasarse
                    Phi_counter = 0 #Se reinicia
                    Phi_environ.pop() #Y sacamos una Phi
            input("CONT")
            os.system('clear') #Limpiamos la pantalla por comodidad

        print("La vida ha cesado...")
        return count_FPrima, count_Phi, count_Beta, count_A, count_B, count_F #Regresamos las listas de conteo de ambientes

    def graficar(): #Función para graficar los resultados de la simulación usando MatPlotLib
        fprimavals = np.array(l1)
        phivals = np.array(l2)
        betavals = np.array(l3)
        avals = np.array(la)
        bvals = np.array(lb)
        fvals = np.array(lf)
        x = np.array(x_vals)
        np.array(fprimavals)
        np.array(phivals)
        np.array(betavals)
        np.array(avals)
        np.array(bvals)
        np.array(fvals)
        print(len(fprimavals))
        print(len(betavals))
        print(len(phivals))
        print(len(x))
        plt.xlabel("Ciclos")
        plt.ylabel("Enzimas y Substratos")
        plt.plot(x, l1, label='fPrima')
        plt.plot(x, phivals, label='Phi')
        plt.plot(x, betavals, label='Beta')
        #plt.plot(x, avals, label='A')
        plt.plot(x, bvals, label='B')
        plt.plot(x, fvals, label='F')
        plt.legend(loc='upper left')
        plt.show()

    l1, l2, l3, la, lb, lf = celula() #Asignamos los resultados de una simulación de un Sistema-(M,R) a las listas que serán graficadas.
    graficar()

if __name__ == "__main__":
    main()
