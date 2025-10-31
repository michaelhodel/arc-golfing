def p(g,R=range):
 for _ in R(4):
  g=[*map(list,zip(*g[::-1]))]
  for I in R(81):
   if(r:=g[i:=I//9])[j:=I%9]*r[j+1]*g[i+1][j]:
    for x in R(2,10-max(i,j)):g[i+x][j+x]=r[j]
 return g