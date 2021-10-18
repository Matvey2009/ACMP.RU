program h;
var N, G, D, i: integer;

begin
  read(N);
  for i := 1 to N do
  begin
    read(G);
    if G > i then
      D := D + G;
  end;
  writeln(D);
end.