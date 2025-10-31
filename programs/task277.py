def p(g,n=range(10),C=(-1,0,1),c=2):
 def H(o):
  for _ in n:o|={(x,y)for X,Y in o for x,y in[(X+x,Y+y)for x in C for y in C]if(10>x>-1<y<10)and g[x][y]}
  return frozenset(o)
 for o in sorted({H({(i,j)})for i in n for j in n if g[i][j]},key=len):
  for i,j in o:g[i][j]=c
  c=1
 return g