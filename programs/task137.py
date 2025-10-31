def p(g):
 R=range(len(g));S=[(i,j)for i in R for j in R];a,(X,Y),_=[(i,j)for i,j in S if g[i][j]]
 for i,j in{(i,j)for i,j in S if max(abs(i-X),abs(j-Y))%(X-a[0])<1}:g[i][j]=g[X][Y]
 return g