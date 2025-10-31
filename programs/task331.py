def p(g,R=range(10)):
 for A in[((7,i,j-1),(6,i,j+1),(2,i-1,j),(8,i+1,j))for i in R for j in R if g[i][j]]:
  for c,x,y in A:
   if 10>x>-1<y<10:g[x][y]=c
 return g