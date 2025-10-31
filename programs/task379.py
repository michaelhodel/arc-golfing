def p(g,n=enumerate):
 for _ in[0]*4:
  for r in(g:=[r for *r,in zip(*g[::-1])]):
   if(2 in r)and(8 in r[(I:=r.index(2)):]):J=r[I:].index(8);r[I:I+J]=[2]*J
 for i,j in{(i,j)for i,r in n(g)for j,e in n(r)if(e==8)*((2 in r[j-1:j+2])+(2 in[*zip(*g)][j][i-1:i+2]))}:
  for a in-1,0,1:g[i+a][j-1:j+2]=8,8-6*(a==0),8
 return g