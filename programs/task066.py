def p(g):
 def T(i,j,g,x,y):
  while h>i>-1<j<h and g[i][j]%3<1:g[i][j]=3;i+=x;j+=y
  return i-x,j-y,g
 for Q in 1,-1:
  for D in-1,1:
   for Z in-1,1:
    l=lambda x:{(i,j)for i,r in N(x)for j,e in N(r)if e==3};N=enumerate;(x,y),(V,W)=l(g);m=abs(x-V);n=abs(y-W);h=len(g);K,L,G=T(*T(*T(x,y,[*map(list,g)],Q*m,Q*n),D*n,D*m),Z*m,Z*n);X=K+Z*m;Y=L+Z*n
    if all(h-1>i>0<j<h-1 for i,j in l(G))and g[X][Y]<3:return G