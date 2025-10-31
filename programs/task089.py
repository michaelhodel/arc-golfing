def p(g):
 n=enumerate;O=[{(i,j,c)}for i,r in n(g)for j,c in n(r)if c]
 for _ in g:O=[o|{(x,y,g[x][y])for X,Y,c in o for x,y in[(X+x,Y+y)for x in(-1,0,1)for y in(-1,0,1)]if 13>x>-1<y<13 and g[x][y]}for o in O]
 for S in O:
  for D in O:
   x,y,C=[x for x in S if x[2]in(2,3)][0]
   if(len(D)<2)*((X:=[*D][0])[2]in[*zip(*S)][2]):
    for a,b,e in S:g[X[0]-x+a][X[1]-([b-y,y-b][C>2])]=e
 return g