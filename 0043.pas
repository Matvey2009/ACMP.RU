Program n0043;
Var 
       n:String;
       count, temp:Integer;
Begin
  count := 0;
  temp := 0;
  readln(n);
  For var i := 1 to length(n) do
  Begin
     if copy(n, i, 1) = '0' then
     begin
         temp := temp + 1;
         if temp > count then
           count := temp;
     end
     else
           temp := 0;
   End;
   writeln(count);
End.