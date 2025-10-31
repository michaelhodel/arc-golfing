def p(g):
 for Y in range(256):
  g=[r[::-1]for*r,in zip(*g)]
  for x in range(10-max(i:=Y//32,j:=Y//4%8)):g[i+x][j+x]|=g[i][j]*(min(g[i][j:j+2]+g[i+1][j:j+2]+g[i+2][j+2:j+3])>0)
 return g