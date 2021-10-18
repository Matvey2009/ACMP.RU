program G;

var
  N, X, Y, S: integer;

begin
  S := 0;
  read(N, X, Y);
  if N mod 3 > 0 then
  begin
    N := N - 5;
    S := S + 1;
    end
    
  else
  begin
    if N mod 3 > 0 then
    begin
      N := N - 5;
      S := S + 1;
    end;
    
    end;
    S := S + (N div 3);
  
  writeln(S)

end.