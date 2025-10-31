def p(g):
 for X in range(324):
  c=X//18;l=X%18;E,k,W=g[c:c+3];J=l+3
  if sum(E[l:J]+k[l:J]+W[l:J])<1:E[l:J]=k[l:J]=W[l:J]=[1]*3
 return g