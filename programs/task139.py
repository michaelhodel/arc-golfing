def p(g,R=range(8)):
 for x in R:
  for i in R:
   for j in R:
    if((r:=g[i+1])[j+1]<1)*min(r[j],g[i][j+1]):r[j+1]=7
  g=[*map(list,zip(*g[::-1]))]
 return g