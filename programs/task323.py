def p(g):
 for _ in 1,1:
  g=[r[::-1]for r in g[::-1]];i,j=divmod(sum(g,[]).index(8),13)
  for c in range(24):
   f=c%4>1;i+=f-1;j+=f
   if(i>-1)*(j<13):g[i][j]=5
 return g