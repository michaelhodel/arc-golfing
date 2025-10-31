def p(g):
 R=range;Z=R(-10,10);F=lambda c:{(i,j)for i in R(10)for j in R(10)if g[i][j]==c};G=F(5)
 for c in{*sum(g,[])}:
  for x in Z:
   for y in Z:
    o=F(c);O={(i+x,j+y)for i,j in o}
    if({(x,y)for X,Y in O for x,y in[(X-1,Y),(X+1,Y),(X,Y-1),(X,Y+1)]}-O-G==G-G)*(O-G==O):
     for i,j in o:g[i][j]=0;g[i+x][j+y]=c
 return g