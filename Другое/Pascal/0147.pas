program p;
var n, x,  x1, x2: integer;
begin
  readln(n);
  x1 := 0;
  x2 := 1;
  for var i := 1 to n do
  begin
    x := x1+ x2;
    x2 := x1;
    x1 := x;
  end;
writeln(x);
end.

