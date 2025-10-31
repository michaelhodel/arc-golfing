def p(g):
 R=range;I=J=0
 for i in R(2,r:=len(g)+1):
  for j in R(c:=len(g[0])+1):
   for x in R(r-i):
    for y in R(c-j):
     if(i*j>I*J)*all(1-any(g[z][y:y+j])for z in R(x,x+i)):I,J,X,Y=i,j,x,y
 for a in R(X,X+I):g[a][Y:Y+J]=[6]*J
 return g