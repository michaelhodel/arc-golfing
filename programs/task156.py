def p(g,n=enumerate):
 O=[{(i,j)}for i,r in n(g)for j,e in n(r)if e]
 for _ in g*2:O=[o|{(x,y)for X,Y in o for x,y in[(X-1,Y),(X+1,Y+1),(X,Y-1)]if 10>x>-1<y<10 and g[x][y]}for o in O]
 for I,o in n(sorted(O,key=len)[::len(O)-1]):
  for i,j in o:g[i][j]-=(3-I)*({(i-1,j),(i+1,j),(i,j-1),(i,j+1)}-o==o-o)
 return g