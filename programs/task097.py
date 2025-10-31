def p(g,n=enumerate):
 for i,j in(S:={(i,j)for i,r in n(g)for j,e in n(r)if e}):g[i][j]*=len(S&{(i+x,j+y)for x in(-1,0,1)for y in(-1,0,1)})>1
 return g