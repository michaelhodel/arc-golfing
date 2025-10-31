def p(g):
 for k in range((d:=len(g)-1)*d):
  if g[i:=k//d][j:=k%d]+g[i+1][j+1]>9:g[i-1][j-1:j+3:3]=1,2;g[i+2][j-1:j+3:3]=3,4
 return g