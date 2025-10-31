def p(g):
 def C(g):
  O=[{(i,j,c)}for i,r in n(g)for j,c in n(r)if c]
  for _ in g:O=[o|{(x,y,g[x][y])for X,Y,c in o for x,y in[(X-1,Y),(X+1,Y),(X,Y-1),(X,Y+1)]if len(g)>x>-1<y<len(g[0])and g[x][y]}for o in O]
  return O
 Z=range(-20,20);n=enumerate;s=sum(g,[]);M=max({*s}-{0},key=s.count);O={(i,j,c)for i,r in n(g)for j,c in n(r)if 0<c!=M};R=lambda x:[*zip(*x[::-1])];
 for o in sum([[*C(x),*C(x[::-1])]for x in(g,R(g),R(R(R(g))))],[]):
  for x in Z:
   for y in Z:
    if len(o)>3==len((s:={(i+x,j+y,c)for i,j,c in o})&O):
     for i,j,c in s:g[i][j]=c
  if o in C(g):
   for i,j,c in o:g[i][j]=0
 return g