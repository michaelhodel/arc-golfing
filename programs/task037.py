def p(g):
 t=range;a=len(g);u={}
 for n in t(a):
  for r in t(a):
   if(i:=g[n][r]):u[i]=u.get(i,[])+[(n,r)]
 for i in u:
  (n,p),(r,d)=u[i];a=(r>n)*2-1;d=(d>p)*2-1
  for r in t(abs(r-n)+1):g[n+r*a][p+r*d]=i
 return g