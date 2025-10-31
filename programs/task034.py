def p(g,R=range):
 for Y in R(256):
  g=[*map(list,zip(*g[::-1]))]
  if(g[i:=Y//32][j:=Y//4%8]==2)*(g[i+1][j+1]+g[i+1][j]+g[i][j+1]<1):
   for x,y in(0,0),(1,0),(0,1):
    for a in R(9-max(i+x,j+y)):g[i+a+x][j+a+y]=max({*sum(g,[])}-{2})
 return g