def p(g):
 d={}
 for i,r in enumerate(g):
  if 4 in r:
   x=r.index(4);y=r.index(4,x+1)
   for t in g[d.setdefault((x,y),i)+1:i]:t[x+1:y]=[2]*~(x-y)
 return g