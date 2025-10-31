def p(g,c=0):
 for I in range(19,1,-1):i=I//2;x=('5, '*i)[:-2];c+=x in(g:=str([*zip(*g)]));g=eval(g.replace(x,(f'{[1,4,2][c-1]}, '*i)[:-2]))
 return g