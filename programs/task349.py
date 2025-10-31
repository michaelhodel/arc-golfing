def p(g):
 h=len(g);n=range;U=lambda o:{(x,y)for X,Y in o for x,y in[(X+x,Y+y)for x in(-1,0,1)for y in(-1,0,1)]};Z=eval(str(g))
 for o in[{(i,j)}for i in n(h)for j in n(h)if Z[i][j]]:
  for _ in g:o|={(x,y)for x,y in U(o)if h>x>-1<y<h and Z[x][y]}
  (a,*_,c),(b,*_,d)=map(sorted,zip(*o));V=c-a;D=(max(V,d-b)+1)//2
  for _ in n(D):o=U(o)
  for i,j in o:
   if h>i>-1<j<h and g[i][j]<2:g[i][j]=3
  for X in n(min(h,a+V+D),h):
   for Y in n(b,d+1):g[X][Y]|=1
 return g