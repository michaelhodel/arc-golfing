def p(g):
 R=range;i,j=map(min,zip(*{(i,j)for i in R(10)for j in R(10)if g[i][j]}))
 for X in R(25):x=X//5;y=X%5;g[i+x][j+y]|=g[i+4-x][j+4-y]|g[i+4-y][j+x]|g[i+y][j+4-x]
 return g