Problem:    servicios
Rows:       6
Columns:    3
Non-zeros:  12
Status:     OPTIMAL
Objective:  z = 56000 (MAXimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 z            B          56000                             
     2 program      B            400                         600 
     3 almacenamiento
                    NU           320                         320           200 
     4 max_obs      B             40                         120 
     5 min_obs      NL            40            40                        -200 
     6 max_vos      B              0                          80 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 X1           B            120             0               
     2 X2           NL             0             0                        -150 
     3 X3           B             40             0               

Karush-Kuhn-Tucker optimality conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.DE: max.abs.err = 0.00e+00 on column 0
        max.rel.err = 0.00e+00 on column 0
        High quality

KKT.DB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
