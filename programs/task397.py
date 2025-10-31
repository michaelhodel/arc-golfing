def p(g,R=range):
 for i in R(9,1,-1):
  for j in R(9):
   if all(S:=g[i-1][j:j+2]+g[i-2][j:j+2]):
    for a in R(len({*S})):g[i+a][j:j+2]=3,3
 return g