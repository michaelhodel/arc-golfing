def p(g):
 (i,j),(x,y)=[divmod(sum(g,[]).index(c),len(g[0]))for c in(8,2)];g[x][j]=4
 for I,*S in(0,i,x),(1,j,y):
  for X in range(min(S)+1,max(S)):g[[X,x][I]][[j,X][I]]=4
 return g