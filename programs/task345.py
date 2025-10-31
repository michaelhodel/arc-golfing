def p(g):
 for y in range(9):
  for x in range(10):
   b,a=g[8-y:10-y]
   if a[x]%5:f=b[x]<1;[a,b][f][x-f+1]=2
 return g