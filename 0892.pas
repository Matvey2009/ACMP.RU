program p;
var N:integer;
Begin
read(N);
if (N = 12) or (N < 3) then write('Winter');
if (N > 2) and (N < 6) then write('Spring');
if (N > 5) and (N < 9) then write('Summer');
if (N > 8) and (N < 12) then write('Autumn');
if N > 12 then write('Error');
End.