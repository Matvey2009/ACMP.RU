program p;
var X1, Y1, X2, Y2, catX, catY: integer;
S: real;

begin
  read(X1, Y1, X2, Y2);
  
  catX := X2 - X1;
  catY := Y2 - Y1;
  S := sqrt((catX * catX) + (catY * catY));
  
  writeln(S:0:5);
end. 