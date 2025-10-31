def p(g):
 n=enumerate;F=sum(3 in r for r in g)>1;S={(i,j)for i,r in n(g)for j,e in n(r)if e%3}
 for o in 0,2:
  for i,j in S:g[i+o*F][j+o*(1-F)]=o
 return g