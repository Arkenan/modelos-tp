from tsp import TSP
from parser import generar_archivo_nodos_aleatorios
import time
import os

def crear_dir_si_no_existe(nombre_dir):
    if not os.path.exists(nombre_dir):
        os.makedirs(nombre_dir)

# Creo las carpetas si no existen.
dir_inputs_tsp_python = "inputs_tsp_python"
dir_inputs_glpk = "inputs_glpk"
crear_dir_si_no_existe(dir_inputs_tsp_python)
crear_dir_si_no_existe(dir_inputs_glpk)

# Cantidad de nodos para cada prueba.
cantidades = [10, 25, 35, 50, 100, 200]

for cant in cantidades:
    print ("problema de " + str(cant) + " clientes.")
    # Archivo aleatorio de input para el TSP por heurística.
    f_tsp_python = dir_inputs_tsp_python + "/" + str(cant) + "clientes.txt"
    generar_archivo_nodos_aleatorios(f_tsp_python, cant)

    tsp = TSP(f_tsp_python)
    # Generación de archivo de input para glpk.
    tsp.to_glpk(dir_inputs_glpk + "/" + str(cant) + "clientes.dat")
    # Solución por heurísticas y medición del tiempo.
    start = time.time()
    print(tsp.sol_insercion_mas_cercana())
    end = time.time()
    print("Tardó " + str(end-start) + " segundos.")
