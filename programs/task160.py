def p(g,R=range(8)):
 for i in R:
  for j in R:
   if all(g[i][j:j+3])*g[i+1][j]:
    for o in 0,1,2:g[i+o][j:j+3]=(X:=2*(o==1)),2,X
 return g