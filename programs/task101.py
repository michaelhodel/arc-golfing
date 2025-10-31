def p(g):
 L=range;h=len(g);w=len(g[0]);f=lambda c:{(i,j)for i in L(h)for j in L(w)if g[i][j]==c};B=f(1);R=f(2);K=lambda X:{(i,j)for i,j in R if min(abs(i-x)+abs(j-y)for x,y in X)<2};r=K(K(B)|B);R-=r;F=lambda C,N,I,J:{(i*N+x+I,j*N+y+J)for(i,j)in C for x in L(N)for y in L(N)}
 for X,Y in[(F(r,N,I,J),F(B,N,I,J))for N in L(1,4)for I in L(-3*h,h)for J in L(-3*w,w)]:
  if X-R==({(i+x,j+y)for x in(-1,0,1)for y in(-1,0,1)for i,j in X}-X)&R==R-R:
   for i,j in Y:
    if h>i>-1<j<w:g[i][j]=1
 return g