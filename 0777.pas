program p;
var S, T: integer;

begin
  read(S, T);
  if S < T then
    writeln(T - S)
  else
    writeln(12 - S + T)
end.