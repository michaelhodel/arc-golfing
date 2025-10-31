def p(g):
 for _ in 1,1:
  g=[*map(list,zip(*g))];N=range;(t,*_,b),(l,*_,o)=map(sorted,[*zip(*[(r,c)for c in N(15)for r in N(15)if g[r][c]%5])])
  for r in N(t+1,b):
   for c in N(l+1,o):
    if g[r][c]*g[t][l+2]:g[r][c]=0;g[[2*b-r,2*t-r][r<(t+b)/2]][c]=5
 return g