def p(g):
 g=[r+r for r in g+g];e=enumerate
 for i,j in{(i+x,j+y)for i,r in e(g)for j,c in e(r)for x,y in((-1,1),(1,-1),(1,1),(-1,-1))if c}:
  if len(g)>i>-1<j<len(g[0])and g[i][j]<1:g[i][j]=8
 return g