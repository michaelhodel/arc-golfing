def p(g,n=range(10)):
 for o in[{(i,j)}for i in n for j in n if g[i][j]<5]:
  for _ in g:o|={(x,y)for X,Y in o for x,y in[(X-1,Y),(X+1,Y),(X,Y-1),(X,Y+1)]if 10>x>-1<y<10 and g[x][y]<5}
  for i,j in o:g[i][j]=4-len(o)
 return g