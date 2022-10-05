program acmp0935;
var x1, y1, x2, y2, c1, c2: integer;
begin
  readln(x1, y1, x2, y2);
  if(((x1+y1) mod 2) = 0) then
    c1 := 1
   else
     c1 := 0;
  if(((x2+y2) mod 2) = 0) then
   c2 := 1
  else
   c2 := 0;
  if(c1 = c2) then
    print('YES')
  else
    print('NO');    
end.