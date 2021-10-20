program p;
var N, S, i: integer;

begin
  read(N);
  
  S := 1;
  for i  := 1 to N do
    S := S + i;
  
  writeln(S);
end.