def p(g):
 for _ in 1,1:
  g=[*zip(*g)];R=range(11)
  for i in R:
   for j in R:g[i+2]=[[[e,6][{*g[i][j:j+5:4],*g[i+4][j:j+5:4]}=={1}],1][e<2]for e in g[i+2]]
 return g