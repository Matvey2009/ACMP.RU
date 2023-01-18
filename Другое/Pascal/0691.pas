Program n0691;
var n  : integer;
       bn: string = 'ABCEHKMOPTXY';
       bm:string = '1234567890';
       s:    string;
begin
  readln(n);
  for var i := 1 to n do
  begin
    readln(s);
    if (length(s) = 6) and
       (copy(s, 1,  1) in bn ) and
       (copy(s, 2,  1) in bm) and
       (copy(s, 3,  1) in bm) and
       (copy(s, 4,  1) in bm) and
       (copy(s, 5,  1) in bn ) and
       (copy(s, 6,  1) in bn )
   then
     writeln('Yes')
   else
     writeln('No')
  end;
end.