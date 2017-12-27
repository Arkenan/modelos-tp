glpsol -m tsp.mod -d inputs_glpk/10clientes.dat -o soluciones_glpk/10clientes.sol > soluciones_glpk/10clientes.out
glpsol -m tsp.mod -d inputs_glpk/25clientes.dat -o soluciones_glpk/25clientes.sol > soluciones_glpk/25clientes.out
glpsol -m tsp.mod -d inputs_glpk/35clientes.dat -o soluciones_glpk/35clientes.sol > soluciones_glpk/35clientes.out
glpsol -m tsp.mod -d inputs_glpk/50clientes.dat -o soluciones_glpk/50clientes.sol > soluciones_glpk/50clientes.out
# glpsol -m tsp.mod -d 100clientes.dat -o 100clientes.sol > 100clientes.out
