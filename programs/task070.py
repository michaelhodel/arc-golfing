def p(g,R=range):
 for i in(k:=lambda g:R((f:=[i for i in R(17)if 8 in g[i]])[0],f[-1]+1))(g):
  for j in k([*zip(*g)]):g[i][j]=max(g[i][j],3)
 return g