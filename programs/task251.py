def p(g,R=range):
 for h in R(H:=len(g)):
  for w in R(H):
   for a in R(H-h+1):
    for b in R(H-w+1):
     for E in R(a+1,a+h-1):
      for D in R(b+1,b+w-1):g[E][D]+=(g[E][D]<1)*all([g[e][b]*g[e][b+w-1]for e in R(a,a+h)]+g[a][b:b+w]+g[a+h-1][b:b+w])
 return g