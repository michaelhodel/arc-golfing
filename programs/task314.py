def p(g,S=[(i//8,i%8)for i in range(64)]):
 for i,j in S:
  for(A,a),(B,b)in((i-3,j),(i+3,j)),((i,j-3),(i,j+3)):
   if(A,a)in(S)and(B,b)in(S)and(X:=g[A][a])==g[B][b]:g[i][j]*=X
 return g