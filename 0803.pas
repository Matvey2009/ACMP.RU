program p;
var A, B, K, i: integer;

begin
read(A, B, K);
  
 for i := 1 to K do
   A := A mod B * 10;
  
  writeln(A div B);
end.