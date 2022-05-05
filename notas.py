#PHI
"""
    def catalizarSubstrato(self, ambienteEnzimaticoOrigen: [Enzima], ambienteEnzimaticoDestino: [Enzima], ambienteSubstrato: [Substrato]):
        super().catalizarSubstrato("A")
        eleccionAleatoria = rand.choices([0, 1], [0.5, 0.5])
        #Elegimos aleatoriamente si catalizamos para B o para Beta
        producto = None
        if eleccionAleatoria == 1:
            ComidaB = ambienteSubstrato.pop()
            producto = self.catalizarReparacionF(ComidaB)
        elif eleccionAleatoria == 0:
            ComidaB = ambienteSubstrato.pop()
            producto = self.catalizarReparacionFPrima(ComidaB)
        #Si es producto es una Beta...
        from FPrima import FPrima
        if isinstance(producto, FPrima):
            #La agregamos al ambiente enzimático y también devolvemos al mismo a la enzima que se usó
            ambienteEnzimaticoDestino.append(producto)
            ambienteEnzimaticoOrigen.append(self)
        #Si el producto es una B...
        from F import F
        if isinstance(producto, F):
            #La agregamos al ambiente de comida y devolvemos al ambiente enzimático la enzima que se usó
            print("Agregando comida al ambiente")
            ambienteSubstrato.append(producto)
            ambienteEnzimaticoOrigen.append(self)
        #Si el resultado es un booleano...
        elif isinstance(producto, bool):
            #Es porque la enzima se degradó y no pudimos hacer nada.
            print("Phi se ha degradado")
"""
"""
WHILE CONTENT
            x_vals.append(next(index))
            enzima1 = FPrima_environ.pop(0)
            enzima1.catalizarSubstrato(FPrima_environ, Beta_environ, A_environ)
            enzima2 = Phi_environ.pop(0)
            enzima2.catalizarSubstrato(Phi_environ, FPrima_environ, B_environ)
            enzima3 = Beta_environ.pop(0)
            enzima3.catalizarSubstrato(Beta_environ, Phi_environ, F_environ)
            ya_vals.append(len(Phi_environ))
            yb_vals.append(len(Beta_environ))
            yc_vals.append(len(FPrima_environ))
            plt.cla()
            plt.plot(x_vals, ya_vals)
            plt.plot(x_vals, yb_vals)
            plt.plot(x_vals, yc_vals)
            plt.xlabel("Ciclos")
            plt.ylabel("Cantidad de Beta")
            A_environ.append(A())
            print("Beta")
            print(Beta_environ)
            print("FPrima")
            print(FPrima_environ)
            print("Phi")
            print(Phi_environ)
            print("F")
            print(F_environ)
            print("B")
            print(B_environ)
            print("A")
            print(A_environ)
            input("Press Enter to continue...")
"""