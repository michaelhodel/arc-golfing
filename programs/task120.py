def p(g,R=range):
 for i in R(len(g)-2):
  for j in R(len(g[0])-2):
   if all(g[i+a][j+a]for a in R(3)):g[i+1][j+1]=8
 return g