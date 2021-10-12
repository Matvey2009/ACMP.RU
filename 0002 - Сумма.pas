Program P;
var N:integer;
begin
ReadLn(N);
if N > 10000 then exit;
if N > 0 then writeln((N+1)*(N/2))
else writeln(-((abs(N) + 1) * (abs(N) / 2)-1))
end.