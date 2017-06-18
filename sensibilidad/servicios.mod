var X1 >= 0;
var X2 >= 0;
var X3 >= 0;

maximize z: 400*X1 + 250*X2 + 200*X3;

s.t. program: 3*X1 + X2 + X3 <= 600;
s.t. almacenamiento: 2*X1 + 2*X2 + 2*X3 <= 320;
s.t. max_obs: X3 <= 120;
s.t. min_obs: X3 >= 40;
s.t. max_vos: X2 <= 80;

end;
