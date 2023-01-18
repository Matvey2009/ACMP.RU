program L;
var S, K, P, C :integer;
begin
read(S);
P := S div 6;
C := S div 6;
K := S - (P + C);
write(P, ' ', K, ' ', C);
end.