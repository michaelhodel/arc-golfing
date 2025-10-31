def p(g):
 h=len(g);w=len(g[0]);s=sum(g,[]);k=s.index(8);d=s[k+w-1:k+w]==[8]
 for a in-1,1:
  b=a-2*a*d;y,x=divmod(k,w)
  while h>y+a>-1<x+b<w:
   Y=y+a;X=x+b;R=g[Y];v=R[X]
   if v-2:y,x=Y,X;R[X]=v or 3
   a*=2*(R!=[2]*w)-1;b*=2*any(2!=r[X]for r in g)-1
 return g