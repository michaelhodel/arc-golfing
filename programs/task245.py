def p(g):
 n=enumerate;R={(i,j)for i,r in n(g)for j,e in n(r)if e%3};X,Y=map(min,zip(*R));Z=sum(g,[]).index(3);d=len(g[0])
 for i,j in R:g[i][j]=0
 for i,j in R:g[Z//d+i-X+1][Z%d+j-Y+1]=2
 return g