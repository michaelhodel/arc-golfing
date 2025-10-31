def p(g):
 d=len;n=enumerate;q=lambda x:[x,[*zip(*x)]][d(g)<d(g[0])];h=q(g);i,j=[k for k,r in n(h)if max(r)]
 for l,k in n(range(i,d(h),j-i)):h[k]=[max(h[[i,j][l%2]])]*d(h[k])
 return q(h)