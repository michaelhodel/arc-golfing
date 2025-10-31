def p(g):
 for X in range(64):g[i:=X//8+1][j:=X%8+1]//=1+(g[i-1][j-1]*g[i+1][j+1]>0)
 return g