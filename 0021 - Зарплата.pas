program p;
var A, B, C, min, max:integer;
begin
read(A, B, C);
if (A >= B) and (A >= C) then max := A;
if (B >= A) and (B >= C) then max := B;
if (C >= B) and (C >= A) then max := C;
 
if (A <= B) and (A <= C) then min := A;
if (B <= A) and (B <= C) then min := B;
if (C <= B) and (C <= A) then min := C;
write(max - min);
end.