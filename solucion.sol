Problem:    tsp
Rows:       23
Columns:    24 (20 integer, 20 binary)
Non-zeros:  87
Status:     INTEGER OPTIMAL
Objective:  z = 9 (MINimum)

   No.   Row name        Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 z                           9                             
     2 salida[0]                   1             1             = 
     3 salida[1]                   1             1             = 
     4 salida[2]                   1             1             = 
     5 salida[3]                   1             1             = 
     6 salida[4]                   1             1             = 
     7 llegada[0]                  1             1             = 
     8 llegada[1]                  1             1             = 
     9 llegada[2]                  1             1             = 
    10 llegada[3]                  1             1             = 
    11 llegada[4]                  1             1             = 
    12 subTours[1,2]
                                   3                           3 
    13 subTours[1,3]
                                   1                           3 
    14 subTours[1,4]
                                   2                           3 
    15 subTours[2,1]
                                   1                           3 
    16 subTours[2,3]
                                   2                           3 
    17 subTours[2,4]
                                   3                           3 
    18 subTours[3,1]
                                   3                           3 
    19 subTours[3,2]
                                  -2                           3 
    20 subTours[3,4]
                                   1                           3 
    21 subTours[4,1]
                                  -2                           3 
    22 subTours[4,2]
                                  -3                           3 
    23 subTours[4,3]
                                   3                           3 

   No. Column name       Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 y[1,2]       *              1             0             1 
     2 y[1,3]       *              0             0             1 
     3 y[1,4]       *              0             0             1 
     4 y[2,1]       *              0             0             1 
     5 y[2,3]       *              0             0             1 
     6 y[2,4]       *              0             0             1 
     7 y[3,1]       *              1             0             1 
     8 y[3,2]       *              0             0             1 
     9 y[3,4]       *              0             0             1 
    10 y[4,1]       *              0             0             1 
    11 y[4,2]       *              0             0             1 
    12 y[4,3]       *              1             0             1 
    13 y[0,1]       *              0             0             1 
    14 y[0,2]       *              0             0             1 
    15 y[0,3]       *              0             0             1 
    16 y[0,4]       *              1             0             1 
    17 y[1,0]       *              0             0             1 
    18 y[2,0]       *              1             0             1 
    19 y[3,0]       *              0             0             1 
    20 y[4,0]       *              0             0             1 
    21 u[2]                        3             0               
    22 u[1]                        2             0               
    23 u[3]                        1             0               
    24 u[4]                        0             0               

Integer feasibility conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
