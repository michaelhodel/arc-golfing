def p(g):
 n=enumerate;F=lambda c:{(i,j)for i,r in n(g)for j,e in n(r)if e==c}
 for c in{*sum(g,[])}-{0,g[0][2]}:
  for i,j in(S:=F(c)):
   for x,y in S:
    for a,b in F(0):g[a][b]+=c*((a==i==x)*(j<b<y)+(i<a<x)*(b==j==y))
 return g