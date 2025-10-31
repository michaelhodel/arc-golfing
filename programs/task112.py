def p(g):
 f=u=0;e=enumerate
 for i,r in e(g):
  for o,G in e(r):f+=i*(G>2);u+=o*(G>2)
 f>>=1;u>>=1
 for i,r in e(g):
  for o,G in e(r):
   if G%3:r[o]=g[f-i][o]=g[i][u-o]=g[f-i][u-o]=2
 return g