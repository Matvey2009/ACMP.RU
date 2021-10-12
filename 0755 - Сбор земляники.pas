program p;
var X, Y, Z, H:integer;
begin
  read(X, Y, Z);
  if (X > 1000) or (Y > 1000) or (Z > 1000) then exit;
  H := X + Y - Z;
  if X + Y < Z then write('Impossible')
  else write(H);
end.