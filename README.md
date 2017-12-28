# Trabajo Práctico 4 de Modelos y Optimización

El problema del viajante definido es asimétrico, ya que los nodos constan de dos puntos (salida y destino) y la distancia entre estos se mide como `d(n1,n2) = d(destino_nodo_1, salida_nodo_2)`.

## Solución Aproximada (Python)

Para esta sección no hay prerrequisitos. El programa se ejecuta con

```bash
python main.py
```

y crea problemas aleatorios del viajante de comercio (TSP) para distintas cantidades de nodos. La clase utilizada para resolverlos es `TSP`, definida en `tsp.py` y todo lo referente a leer y escribir archivos está en el módulo `parser.py`. La solución implementada es por Inserción Más cercana.

Además de calcular las soluciones para esos problemas aleatorios, el script deja en la carpeta `inputs_glpk` los archivos de datos correspondientes a esos problemas para poder ejecutar sus soluciones exactas.

## Solución Exacta con PLE (glpk)

Para esta sección es necesario tener GLPK instalado. La solución a todos los problemas creados en la sección anterior se calcula con:

```bash
sh glpk.sh
```

Este deja en la carpeta `soluciones_glpk` los archivos de salida. Actualmente el archivo tiene comentado el problema de 100 clientes y no tiene el de 200, ya que su ejecución tardaba demasiado en la computadora utilizada para el desarrollo.
