def p(g):
 n=enumerate;(a,A),*_,(b,B)=P=[(y,x)for y,r in n(g)for x,v in n(r)if v]
 for t,(y,x)in n(P):
  for u in-1,0,1:
   for v in-1,0,1:
    if u|v:g[y+u][x+v]=g[a][[B,A][0<t<3]]
 for i in range(2,(b-a)//4*2+1,2):g[a+i][A]=g[a+i][B]=g[b-i][A]=g[b-i][B]=5
 for i in range(2,(B-A)//4*2+1,2):g[a][A+i]=g[a][B-i]=g[b][A+i]=g[b][B-i]=5
 return g