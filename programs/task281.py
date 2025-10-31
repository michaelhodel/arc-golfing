def p(g):
 n=enumerate;s=sum(g,[]);(i,*_,j),(k,*_,l)=[[i for i,r in n(G)if max(r)]for G in(g,zip(*g))]
 for o,c in n(sorted({*s}-{0,8},key=s.index)):
  for x in range(i+o,j+1-o):g[x][k+o:l+1-o]=[c]*(l+1-2*o-k)
 return g