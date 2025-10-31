def p(g,N=enumerate):
 for _,_ in N(g[:4]):
  for i,r in N(g:=[*map(list,zip(*g[::-1]))]):
   for j,e in N(r):r[j]+=2*(g[i-1][j]*r[j-1]*(e<1)>0)
 return g