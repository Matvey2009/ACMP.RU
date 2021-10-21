program p;
var A, B, S, i: integer;

begin
  read(A, B);
 
  for i := 1 to A * B do
  begin
    S := A * i;
    if S mod B = 0 then
      break;
   
    end;
     writeln(S);
end.