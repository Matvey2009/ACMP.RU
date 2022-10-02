program acmp0844;
var a, b: int64;
       c: real;
begin
  readln(a, b);
  c := sqrt(a*b);
  if (c <> round(c)) then
   c := 0;
  writeln(round(c))
end.