def p(g):
 M=[r.index(max(r))for r in g];I=max(M,key=M.count)+1;m=max(g[I]);N=len(g);P=[[m]*N];h=[[m]+r+[m]for r in P+g+P];R=range
 for i in(X:=R(0,N,I)):
  for j in X:
   for x in(Y:=R(i+1,i+I)):g[x-1][j:j+I-1]=[3*all([h[x][j]*h[x][j+I]for x in Y]+h[i][j+1:j+I]+h[i+I][j+1:j+I])]*(I-1)
 return eval(str(g).replace(*'04'))