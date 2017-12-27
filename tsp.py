from parser import getNodos

# Resolvedor de problemas del viajante de comercio.
class TSP:
    def __init__(self, archivoInput):
        self.nodos = getNodos(archivoInput)
        self.init_distancias()
        self.distancias_inevitables = sum([n.distanciaInterna() for n in self.nodos])

    def init_distancias(self):
        n = len(self.nodos)
        self.distancias = [n*[0] for i in range(n)]
        for (i, n1) in enumerate(self.nodos):
            for (j, n2) in enumerate(self.nodos):
                if i!=j:
                    self.distancias[i][j] = n1.distancia(n2)
        # Además agrego una matriz que incluye al nodo artificial con distancia 0.
        self.distancias0 = [(n+1)*[0]] + [[0] + fila for fila in self.distancias]

    # Solución por heurística de inserción más cercana.
    def sol_insercion_mas_cercana(self):
        # El primer nodo sí o sí será el 0, que tiene distancia 0 a todos.
        # Por ahí convenga usar otro, o random. Por qué el 0?
        tourActual = [0]
        costoActual = 0
        restantes = set(range(1,len(self.nodos)+1))

        # A cada paso agregaremos un nodo de los n restantes.
        for i in range(len(self.nodos)):
            # Tenemos que decidir cuál agregar.
            costoNodoMin = float('inf')
            for nodoSeleccionado in restantes:
                # Y tenemos que ver a dónde queda mejor.
                costoAgregadoMin = float('inf')
                for posicion in range(len(tourActual)):
                    # Si lo inserto en posicion se agregan dos aristas y se va una.
                    costoAgregado = self.distancias0[nodoSeleccionado][tourActual[posicion]]\
                        + self.distancias0[tourActual[posicion-1]][nodoSeleccionado]\
                        - self.distancias0[tourActual[posicion-1]][tourActual[posicion]]
                    # print ("Costo de añadir nodo " + str(nodoSeleccionado) + " en la posicion " + str(posicion) + ": " + str(costoAgregado))
                    # Comparo a ver si esa posición es la mejor hasta ahora.
                    if costoAgregado < costoAgregadoMin:
                        costoAgregadoMin = costoAgregado
                        posMin = posicion
                # A ver si este es el mejor nodo a insertar hasta ahora.
                if costoAgregadoMin < costoNodoMin:
                    costoNodoMin = costoAgregadoMin
                    nodoMin = nodoSeleccionado
                    posNodoMin = posMin
            # Ahora que está seleccionado el nodo lo agrego al tour a donde le corresponde.
            # print("se inserta el nodo " + str(nodoMin) + " en la posición " + str(posNodoMin) + " con costo agregado " + str(costoNodoMin))
            tourActual.insert(posNodoMin, nodoMin)
            restantes.remove(nodoMin)
        # Devuelvo el tour y su costo total.
        return (tourActual, self.distancias_inevitables + \
            sum([self.distancias0[tourActual[i-1]][tourActual[i]] for i in range(len(tourActual))]))

    # Escribe en "archivoOutput" los datos del problema formateados para GLPK.
    def to_glpk(self, archivoOutput):
        fout = open(archivoOutput, "w")

        # Header
        fout.write("# Data Section: TP3 Modelos\n\n")
        fout.write("data;\n\n")
        fout.write("# Conjuntos\n\n")

        n = len(self.nodos)

        # Conjuntos
        fout.write("set VIAJES := ")
        for i in range(1, n):
            fout.write(str(i) + " ")
        fout.write(str(n) + ";\n\n")

        fout.write("set NODOS := ")
        for i in range(0, n):
            fout.write(str(i) + " ")
        fout.write(str(n) + ";\n\n")

        # Matriz

        fout.write("# Matriz de distancias\n\n")
        fout.write("param DISTANCIAS: ")
        for i in range(1,n):
            fout.write(str(i) + " ")
        fout.write(str(n) + ":=\n")

        for i in range(n):
            fout.write(str(i+1) + "                 ")
            for j in range(n):
                if i!=j:
                    fout.write(str(self.distancias[i][j]) + " ")
                else:
                    fout.write(". ")
            if i == n-1: fout.write(";")
            fout.write("\n")

        # Footer

        fout.write("\nend;\n\n")

        # Adjunto como comentario la inevitable suma interna de todos los nodos.

        fout.write("# Suma de distancias internas: C = " + \
            str(self.distancias_inevitables) + "\n")

        fout.close()
