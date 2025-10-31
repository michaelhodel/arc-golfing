def p(g):
 Q=30;U=range;E=[[(1>g[i][j])*all(1-(Q>i+a>-1<j+b<Q)or 1>g[i+a][j+b]for a in(-1,0,1)for b in(-1,0,1)if a|b)for j in U(Q)]for i in U(Q)];h=[0]*Q;R=[]
 for i in U(Q):
  for j in U(Q):h[j]=E[i][j]and h[j]+1
  for L in U(Q):
   if(m:=h[L]):
    for r in U(L,Q):
     if 1>h[r]:break
     m=min(m,h[r]);R+=[(i-k+1,L,i,r,(r-L+1)*k)for k in U(1,m+1)]
 F=lambda x:x[3]-x[1]+1;G=lambda x:x[2]-x[0]+1;R.sort(key=lambda r:(-r[4],r[0],r[1]));A,B=[[r for r in R if X(r)>Y(r)][0]for X,Y in((F,G),(G,F))];I=A and B and[[[B,A][A[4]>=B[4]],B][F(A)<G(B)],A][F(A)>G(B)];L=F(I)<G(I)
 def P(a):
  for i in U(a[0],a[2]+1):g[i][a[1]:a[3]+1]=[3]*F(a)
 P(I);C=[I]
 for r in R:
  if((G,F)[L](r)>4)*(lambda a:1-any(0<=r<Q and 3 in[[*zip(*g)],g][L][r][a[L]:a[L+2]+1]for r in(a[1-L]-1,a[3-L]+1)))(r)*(r[L+2]+1==I[L]or r[L]-1==I[L+2])*(r[1-L]<=I[3-L])*(r[3-L]>=I[1-L])*all(1-(r[1]<=b[3]and b[1]<=r[3]and r[0]<=b[2]and b[0]<=r[2])for b in C):P(r);C+=[r]
 return g