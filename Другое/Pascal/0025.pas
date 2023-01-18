program p;
var A, B:integer;
Begin
    read(A, B);
    if A < B then write('<');
    if A > B then write('>');
    if A = B then write('=');
End.