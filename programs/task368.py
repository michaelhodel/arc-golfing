def p(g):
 P=[[0]*10];R=range;G=[[0,*r,0]for r in P+g+P];S={(i,j)for i in R(10)for j in R(10)if G[i][j+1]==G[i+1][j]<1};X,Y=max(S,key=lambda x:G[x[0]+1][x[1]+1]%5)
 for i,j in S:
  if G[I:=i+1][J:=j+1]:
   for a in R(I,I+4):
    for b in R(J,J+4):
     if G[a][b]:g[a-1][b-1]=G[a-I+X+1][b-J+Y+1]
 return g