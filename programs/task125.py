def p(g):
 n=enumerate;R=[];L=[];P={(i,j)for i,r in n(g)for j,e in n(r)if e%8}
 for i,j in{*sum([[(i+x,j+y)for x in(-1,0,1)for y in(-1,0,1)]for i,j in P],[])}-P:g[i][j]=3
 for X in[g,zip(*g)]:
  for I,r in n(X):
   if 6 in r:L+=sum([[[],[[(k,I)],[(I,k)]][X==g]][r[k]!=6]for k in range(r.index(6)+1,14-r[::-1].index(6))],[])
  R+=[L];L=[]
 for i,j in{*R[0]}&{*R[1]}:g[i][j]=4
 return g