program p;
var N:integer;
begin
  read(N);
  if N > 1000 then exit;
  if (N = 1) or (N = 0) then write(0)
  else if (N mod 2) = 0 then write(N/2)
  else write(N);
end.