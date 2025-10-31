def p(g):
 R=range(1,29);B=max(g[0],key=g[0].count);i,j=[(i,j)for i in R for j in R if(g[i+1][j]==g[i-1][j]!=g[i][j]!=g[i][j+1]==g[i][j-1])*(g[i+1][j+1]!=g[i+1][j]or g[i+1][j+1]!=g[i][j+1])][0]
 for a,b,x,y in[(a,b,x,y)for x,y in[(x,y)for x,y in((-1,0),(1,0),(0,-1),(0,1))if g[i+x][j+y]!=g[i-1][j-1]]for a in R for b in R if(2<abs(a-i)+abs(b-j))*(g[a][b]==g[i][j])]:
  for o in(-1,0,1):g[a+o][b-1:b+2]=[[e,g[a-1][b-1]][e==B]for e in g[i+o][j-1:j+2]]
  for k in R:
   if g[X:=a+x*k][Y:=b+y*k]==B:break
   g[X][Y]=g[a+x][b+y]
 for x in range(i-2,i+3):g[x][j-2:j+3]=[B]*5
 return g