class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def dist(self, otro):
        return abs(otro.x - self.x) + abs(otro.y - self.y)

class Nodo:
    def __init__(self, cx, cy, dx, dy):
        self.c = Punto(cx, cy)
        self.d = Punto(dx, dy)

    def distancia(self, otro):
        return self.d.dist(otro.c)

    def distanciaInterna(self):
        return self.d.dist(self.c)

class Parser:
    def __init__(self, archivoInput):
        self.fin = open(archivoInput)

    def getNodos(self):
        nodos = []
        # Por el momento se asume que el input está bien formado.
        for line in self.fin:
            vals = line.split()
            nodos.append(Nodo(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3])))

        return nodos

    # TODO eliminar archivo de entrada en destructor.

class TSP:
    def __init__(self, archivoInput):
        self.nodos = Parser(archivoInput).getNodos()
        self.init_distancias()

    def init_distancias(self):
        n = len(self.nodos)
        self.distancias = [n*[0] for i in range(n)]
        for (i, n1) in enumerate(self.nodos):
            for (j, n2) in enumerate(self.nodos):
                if i!=j:
                    self.distancias[i][j] = n1.distancia(n2)
        # Además agrego una matriz que incluye al nodo artificial con distancia 0.
        self.distancias0 = [(n+1)*[0]] + [[0] + fila for fila in self.distancias]

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
                for posicion in range(len(tourActual)+1):
                    # Si lo inserto en posicion se agregan dos aristas y se va una.
                    costoAgregado = self.distancias0[nodoSeleccionado][posicion]\
                        + self.distancias0[posicion-1][nodoSeleccionado]\
                        - self.distancias0[posicion-1][posicion]
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
            print("se inserta el nodo " + str(nodoMin) + " en la posición " + str(posNodoMin))
            tourActual.insert(posNodoMin, nodoMin)
            restantes.remove(nodoMin)
        # Devuelvo el tour y su costo total.
        return (tourActual, sum([self.distancias0[i-1][i] for i in range(len(tourActual))]))

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
            str(sum([n.distanciaInterna() for n in self.nodos])) + "\n")

        fout.close()
