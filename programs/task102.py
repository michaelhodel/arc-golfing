def p(g,r=range):
 for X in r(6):
  for J in r((D:=13-(d:=X+3))*D):
   if min(g[(x:=J//D)+(i:=I//d)][(y:=J%D)+(j:=I%d)]*(F:={i,j}&{0,d-1}!=set())+(g[x+i][y+j]<1)*(1-F)for I in r(d*d)):
    for i in r(x+1,x+d-1):g[i][y+1:y+d-1]=[2]*(d-2)
 return g