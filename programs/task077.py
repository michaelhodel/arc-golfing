def p(g,N=enumerate):
 for i,j in(s:={(i,j)for i,r in N(g)for j,e in N(r)if e==2}):
  o={(i,j)};n={0}
  while n:n={(x,y)for x,y in s if min(max(abs(x-v),abs(y-w))for v,w in o)<3}-o;o|=n
  a,b=[range(min(x),max(x)+1)for x in zip(*o)]
  for x in a:
   for y in b:g[x][y]=(g[x][y]!=2)*2+2
 return g