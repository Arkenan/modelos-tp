from random import randint
from nodos import Nodo

# Parsea el archivo de input y devuelve sus nodos.
def getNodos(fin_name):
    fin = open(fin_name)

    nodos = []
    # Por el momento se asume que el input está bien formado.
    for line in fin:
        vals = line.split()
        nodos.append(Nodo(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3])))

    fin.close()

    return nodos

def generar_archivo_nodos_aleatorios(fout_name, cantNodos):
    fout = open(fout_name, 'w')

    for n in range(cantNodos):
        fout.write(str(randint(0,cantNodos)) + " " + str(randint(0,cantNodos)) + " " \
            + str(randint(0,cantNodos)) + " " + str(randint(0,cantNodos)) + "\n")

    fout.close()
