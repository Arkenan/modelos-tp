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
