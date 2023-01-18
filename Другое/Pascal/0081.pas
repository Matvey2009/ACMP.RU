program p;
var N, X, min, max, i:integer;
begin
readln(N);
max := 0;
min := 30000;
for i := 1 to N do
begin
read(X);
if X > max then max := X;
if X < min then min := X;
end;
write(min, ' ', max);
end.