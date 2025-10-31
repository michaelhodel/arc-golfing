def p(g,R=range):
 for I in R(3):
  for X in R((F:=10-I)*F):
   if{*g[i:=X//F][(j:=X%F):j+(d:=I+3)]+g[i+d-1][j:j+d],g[i+1][j]}=={5}:
    for x in R(i+1,i+d-1):g[x][j+1:j+d-1]=[I+6]*(d-2)
 return g