program p;
var N, K, M, G, H: integer;

begin
  read(N, K, M);
  
  G := N div (K + M) * 2;
  H := N - G * (K +M) div 2;
  if H = 0 then
    G := G
  else if H > K then
    G := G + 2
    else
      G := G + 1; 
  
  writeln(G);
end.