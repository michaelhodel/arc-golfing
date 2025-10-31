def p(g,n=enumerate):
 for C in{*sum(g,[])}-{0}:
  (a,*_,b),(c,*_,d)=map(sorted,zip(*{(i,j)for i,r in n(g)for j,e in n(r)if e==C}))
  for r in g[a:b+1]:r[c:d+1]=[C]*(d-c+1)
 return g