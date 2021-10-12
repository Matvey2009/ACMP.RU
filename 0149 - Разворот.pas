program p;
var N, i : integer;
  arr : array of integer;
begin
read(N);
setLength(arr, N);
if abs(N) > 1000 then exit;
for i:=0 to N-1 do
  read(arr[i]);
for i:=N-1 downto 0 do
  write(arr[i], ' ');
end.