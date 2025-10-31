def p(g):
 R=range(19);_,Y,X,t=min([(sum(t:=[r[x:x+3]for r in g[y:y+3]],g).count(0),y,x,t)for y in R for x in R])
 for a in-4,0,4:
  for b in-4,0,4:
   for k in R:
    for I in[*R][:9]:
     if a|b!=0<=(x:=X+b*k)+(j:=I%3)<21>(y:=Y+a*k)+(i:=I//3)>=0<k:g[y+i][x+j]=t[i][j]and max(max(r[X+b:X+b+3])for r in g[Y+a:Y+a+3])
 return g