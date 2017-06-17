/* TP3 Modelos y Optimizacion I: Modelo */

# Conjuntos

set VIAJES;
set NODOS;


# Variables

var y{i in NODOS, j in NODOS} >= 0, binary;
var u{i in VIAJES} >= 0;


# Parámetros

param DISTANCIAS{i in VIAJES, j in VIAJES};


/* Funcional */

minimize z: sum{i in VIAJES,j in VIAJES : i <> j} DISTANCIAS[i,j] * y[i,j];


/* Restricciones */

/* Solo se puede salir una vez de cada lugar */

s.t. salida  {i in NODOS}: sum{j in NODOS: i <> j} y[i,j] = 1;


/* Solo se puede llegar una sola vez a cada lugar */

s.t. llegada {j in NODOS}: sum{i in NODOS: i <> j} y[i,j] = 1;


/* Evitar Subtours */

s.t. subTours {i in VIAJES, j in VIAJES: i <> j}: u[i] - u[j] + card(VIAJES) * y[i,j] <= card(VIAJES) - 1;


end;
