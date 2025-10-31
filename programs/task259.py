def p(g):
 for _ in 1,1:a,*_,b=[i for i,r in enumerate(g)if max(r)>1];g=[*zip(*[[e*(e>1)for e in r]for r in g[a:b+1]])]
 return g