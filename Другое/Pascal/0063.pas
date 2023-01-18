program h;
var X, Y, S, P: integer;

begin
  read(S, P);
  
  for X := 0 to S do
  begin
    Y := S - X;
    if X * Y = P then
       begin
        writeln(X, ' ',  Y);
        break;
        end;
  end;
  end.