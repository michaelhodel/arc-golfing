def p(g):
 G=eval(str(g).replace(*'50'));n=range;O=[{(i,j)}for i in n(20)for j in n(20)if G[i][j]]
 for _ in g:O=[o|{(x,y)for X,Y in o for x,y in[(X+x,Y+y)for x in(-1,0,1)for y in(-1,0,1)]if 20>x>-1<y<20 and G[x][y]}for o in O]
 def F(o):x,y=map(min,zip(*o));a,b=[*o][0];return{(i-x,j-y)for i,j in o},g[a][b]
 for a in O:
  for b in O:
   for i,j in a:A,x=F(a);B,y=F(b);I,J=[*b][0];g[i][j]=[x,y][(x<5)*(A==B)*(5 in g[I][:J])*(5 in g[I][J:])]
 return g