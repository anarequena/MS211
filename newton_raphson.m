function nr = newton_raphson(x)
x = -1.5;
k = 0;

f = atan(x);
f1 = 1/(1+(x*x));

x1 = x - f/f1;

while(abs(x1-x) >= 0.000001) %|| abs(f) >= 0.000001)
  x = x1;
  d = -f/f1
  x1 = x + d;
  f = atan(x1)
  f1 = 1/(1 + (x1*x1))
  k = k + 1;
 end