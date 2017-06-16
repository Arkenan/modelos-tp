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

        for (i,n1) in enumerate(self.nodos):
            fout.write(str(i+1) + "                 ")
            for n2 in self.nodos:
                if n1!=n2:
                    fout.write(str(n1.distancia(n2)) + " ")
                else:
                    fout.write("." + (" " if i != len(self.nodos) - 1 else " ;"))
            fout.write("\n")
        # Footer

        fout.write("\nend;\n\n")

        # Adjunto como comentario la inevitable suma interna de todos los nodos.

        fout.write("# Suma de distancias internas: C = " + \
            str(sum([n.distanciaInterna() for n in self.nodos])) + "\n")

        fout.close()
