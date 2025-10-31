def p(g):
 s=sum(g,[]);d=min(s,key=s.count);n=enumerate;O,I=[{(i,j)for i,r in n(g)for j,e in n(r)if e==c}for c in(0,d)];x,y=min([(x,y)for x in(-1,0,1)for y in(-1,0,1)],key=lambda X:I-{(i+X[0],j+X[1])for i,j in O}!=I-I);R=range(1,9);(A,*_,C),(B,*_)=map(sorted,zip(*O));a=[min(a for a in R if{(i+x*a,j+y*a)for i,j in O}&I),C-A][(A,B)in O]+1
 for i,j in O:
  for k in R:
   if len(g)>(I:=i+x*a*k)>-1<(J:=j+y*a*k)<len(g[0]):g[I][J]=d
 return g 