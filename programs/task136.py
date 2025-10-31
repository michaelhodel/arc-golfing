def p(g):
 for c in 1,2:
  g=[r[::-1]for r in g[::-1]];i,j=divmod(sum(g,[]).index(c),10)
  for k in range(10-max(i,j)):g[i+k][j+k]=c
 return g