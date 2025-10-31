def p(g,E=enumerate):
 f=sum(g,[]);Y,X=divmod(f.index(*[c for c in{*f}if"2, 1, 2"in str([r.count(c)for r in g])!=f.count(c)<6]),len(g))
 for y,r in E(g):
  for x,v in E(r):
   if v:g[a:=2*Y+2-y][b:=2*X+2-x]=g[y][b]=g[a][x]=v
 return g